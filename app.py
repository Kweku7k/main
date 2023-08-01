
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import csv
from flask import Flask, jsonify
from flask_cors import CORS




app=Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] =" thisismysecretkey"
#'postgresql://postgres:new_password@45.222.128.225:5432/postgres'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Lecturers(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(20) )
    name= db.Column(db.String(200) )
    password= db.Column(db.String(200) )
    school = db.Column(db.String(20) )
    image= db.Column(db.String(10)  )
    telephone= db.Column(db.String(10)  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.email})"
  
class School(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total = db.Column(db.String() )
    department = db.Column(db.String() )
    school = db.Column(db.String() )
    program = db.Column(db.String()  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.department})"
  
class Department(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total= db.Column(db.String() )
    department = db.Column(db.String() )
    school = db.Column(db.String() )
    program = db.Column(db.String()  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.school})"

class Year(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total= db.Column(db.String() )
    
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}')"
  
  
class Student(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    total= db.Column(db.String() )
    department = db.Column(db.String())
    program = db.Column(db.String())
    email= db.Column(db.String(20))
    school = db.Column(db.String())
    telephone = db.Column(db.String())
    password = db.Column(db.String())
    image= db.Column(db.String()  )
    bio= db.Column(db.String()  )
    current_company= db.Column(db.String()  )
    socials= db.Column(db.String()  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.school})"



@app.route('/uploadCsv', methods=['GET', 'POST'])
def uploadCsv():
    if request.method == 'POST':
         # Read the File using Flask request
        file = request.files['file']
        file.filename = "name.csv"
        # save file in local directory
        file.save(file.filename)
        print(file.filename)
        #return fetchCourseAllocation()
    return render_template('uploadCsv.html')




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




#school get request.
@app.route('/school', methods=['GET', 'POST'])
def school():
    school=School.query.all()
    schools = []
    print(school)
    for s in school:
        schools.append({
            "name":s.name,
            "school":s.school,
            "department":s.department,
            "program":s.program
        })
    print("-------------")
    print(schools)
    print("-------------")
    return schools



#school post request.
@app.route('/post_school', methods=['POST'])
def post_school():
    print(request.get_json())
    body = request.get_json()
    print(body)
    print(body["name"],body["school"],body["department"],body["program"])
    
    newschool = School(name=body["name"], school=body["school"],department=body["department"], program=body["program"])
    
    db.session.add(newschool)
    db.session.commit()
    
    post_schools = School.query.all()
     # Convert the School objects to a list of dictionaries (JSON serializable)
    schools_data = [{"name": school.name, "school": school.school,
                        "department": school.department, "program": school.program}
                    for school in post_schools]
    
    response_body = {
        "data":post_school
    }
    return schools_data

    
    
    
    
#department get request
@app.route("/department")
def department():
    department=Department.query.all()
    departments=[]
    for d in department:
        departments.append({
            "id":d.id,
            "name":d.name,
            "department":d.department,
            "school":d.school,
            "program":d.program
            
        })
    print("-------------")
    print(departments)
    print("-------------")
    return departments

#department post request.
@app.route('/post_department', methods=['POST'])
def post_department():
    print(request.get_json())
    body = request.get_json()
    print(body)
    print(body["name"],body["school"],body["department"],body["program"])
    
    newdepartment = Department(name=body["name"], school=body["school"],department=body["department"], program=body["program"])
    
    db.session.add(newdepartment)
    db.session.commit()
    
    post_department = Department.query.all()
    
     # Convert the School objects to a list of dictionaries (JSON serializable)
    departments_data = [{"name": department.name, 
                         "school": department.school,
                        "department": department.department,
                        "program": department.program}
                    for department in post_department]
    
    response_body = {
        "data":post_department
    }
    return departments_data

    

    
#student get request
@app.route("/student", methods=['GET'])
def student():
    student=Student.query.all()
    students=[]
    print(student)
    for st in student:
        students.append({
            
            "id":st.id,
            "name":st.name,
            "department":st.department,
            "school":st.school,
            "program":st.program,
            "email":st.email,
            "telephone":st.telephone,
            "password":st.password,
            "image":st.image
        })
    print("-------------")
    print(students)
    print("-------------")
    return students


#student post request
@app.route('/post_student', methods=['POST'])
def post_student():
    print(request.get_json())
    body = request.get_json()
    print(body)
    print(body["name"],body["school"],body["department"],body["program"],body['email'],body['telephone'],body['password'],body['bio'],body['current_company'],body['socials'])
    
    newstudents = Student(name=body["name"],
                         school=body["school"],
                         department=body["department"],
                         program=body["program"],
                         telephone=body['telephone'],
                         password=body['password'],
                         email=body['email'],
                         bio=body['bio'],
                         current_company=body['current_company'],
                         socials=body['socials'])
    
    db.session.add(newstudents)
    db.session.commit()
    
    post_student = Student.query.all()
    
     # Convert the School objects to a list of dictionaries (JSON serializable)
    students_data = [{"name": student.name, 
                         "school": student.school,
                        "department": student.school,
                        "program": student.program,
                        "email":student.email,
                        "password":student.password,
                        "telephone":student.telephone,
                        "bio":student.bio,
                        "current_company":student.current_company,
                        "socials":student.socials}
                    for student in post_student]
    
    response_body = {
        "data":post_student
    }
    return students_data


#STUDENT UPDATE
@app.route('/update_student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    #try:
        # Fetch the student record by ID
        student = Student.query.get(student_id)

        #if not student:
            #return jsonify({'error': f'Student with ID #{student_id} not found.'}), 404

        # Get the JSON data from the request's payload
        body = request.get_json()

        # Update the student's information with the provided data
        for key, value in body.items():
            setattr(student, key, value)
        # Commit the changes to the database
        db.session.commit()
        return jsonify({"success":True})

        # Return a success message
        #return jsonify({'message': 'Student information updated successfully.'}), 200

    #except Exception as e:
     #   return jsonify({'error': 'An error occurred: {}'.format(e)}), 500

#STUDENT DELETE
@app.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
        student = Student.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
 
        return jsonify({'message': 'Student deleted successfully.'}), 200


#year get request
@app.route("/year")
def year():
    year=Year.query.all()
    years=[]
    print(year)
    for y in year:
        years.append({
            "name":y.name,
            "total":y.total,
        })
    print("-------------")
    print(years)
    print("-------------")
    return years

# POST route
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({'message': 'Received POST data successfully!', 'data': data})


# GET route
@app.route('/get_data', methods=['GET'])
def get_data():
    response_array=[]
    for s in School.query.all():
        response_array.append(s.data)  
    response_array = {'message': 'This is a GET request.',
                        'name':'Eben'}
    return jsonify(response_array)



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
