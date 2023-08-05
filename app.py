
import pprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import csv
from sqlalchemy import or_
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
        return f"Lecturers('{self.id}', {self.name}', {self.email})"
  
class School(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total = db.Column(db.String() )
    department = db.Column(db.String() )
    school = db.Column(db.String() )
    program = db.Column(db.String()  )
    def __repr__(self):
        return f"School('{self.id}', {self.name}', {self.department})"
  
class Department(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total= db.Column(db.String() )
    department = db.Column(db.String() )
    school = db.Column(db.String() )
    program = db.Column(db.String()  )
    def __repr__(self):
        return f"Department('{self.id}', {self.name}', {self.school})"

class Year(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String() )
    total= db.Column(db.String() )
    
    def __repr__(self):
        return f"Year('{self.id}', {self.name}')"
  
  
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
        return f"Student('{self.id}', {self.name}', {self.school})"
    

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String())
    firstname = db.Column(db.String())
    maiden_name = db.Column(db.String())
    offical_email = db.Column(db.String())
    personal_email = db.Column(db.String())
    password = db.Column(db.String())
    position= db.Column(db.String())
    member_staff = db.Column(db.String())
    department_directorate_unit = db.Column(db.String())
    number = db.Column(db.String())
    gender = db.Column(db.String())
    position = db.Column(db.String())
    rank = db.Column(db.String())
    grade = db.Column(db.String())
    job_title = db.Column(db.String())
    employment_status = db.Column(db.String())
    
    def __repr__(self):
        return f"staff('{self.id}', {self.firstname}', {self.position})"
    

# class Employment(db.Model):
#     date_of_appointment = db.Column(db.Date)
#     date_of_appointment = db.Column(db.Date)
#     end_of_contract = db.Column(db.Date)
    
    

class ID(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ghana_card = db.Column(db.String(100))
    snit_number = db.Column(db.String(100))
    tin_number = db.Column(db.String(100))
    immigration_number = db.Column(db.String(100))
    address = db.Column(db.String(200))
  

class Financial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_number = db.Column(db.String(100))
    bank_name = db.Column(db.String(100))
    bank_branch = db.Column(db.String(100))
    
    
class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    next_of_kin = db.Column(db.String(100))
    relationship = db.Column(db.String(100))
    address_kin = db.Column(db.String(100))
    gender_kin = db.Column(db.String(100))



class Beneficianies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_beneficianies= db.Column(db.String(100))
    address_beneficianies = db.Column(db.String(100))
    other_beneficianies= db.Column(db.String(100))
    gender_beneficianies= db.Column(db.String(100))
   
   
   
@app.route('/', methods=['GET', 'POST'])
def base():
    return render_template("base.html")


@app.route('/staff', methods=['GET', 'POST'])
def uploadCsv():
    responseArray = []
    if request.method == 'POST':
         # Read the File using Flask request
        file = request.files['file']
        file.filename = "name.csv"
        # save file in local directory
        file.save(file.filename)
    
    with open('name.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        responseArray = []

        # for c in CourseAllocation.query.all():
        #     print(c)
        #     db.session.delete(c)

        next(csv_reader)

        for line in csv_reader:
            
            
            # print("316" + "/" + line["No."])
            # print(line)
            print("--------------")
            print(line.get("Id","null"))
            print(line.get("Name","null"))
            print(line.get("UssdCode","null"))
            responseArray.append(line)

            # Course Allocation
            newStaff = Staff(
                surname=(line.get("surname")),
                firstname=(line.get("firstname")),
                maiden_name=(line.get("maiden_name")),
                offical_email=(line.get("offical_email")),
                personal_email=(line.get("personal_email")),
                position=(line.get("position")),
                department_directorate_unit=(line.get("department_directorate_unit")),
                number=(line.get("number")),
                gender=(line.get("gender")),
                rank=(line.get("rank")),  # Add a comma here
                grade=(line.get("grade")),  # Add a comma here
                job_title=(line.get("job_title")),  # Add a comma here
                employment_status=(line.get("employment_status")) 
            )
            print(newStaff)
            db.session.add(newStaff)
        db.session.commit()

        response = {
            "body":responseArray
        }
        print(response)
        pprint.pprint(responseArray)
    return render_template("dashboard.html", response=responseArray)
       

@app.route('/search', methods=['GET','POST'])
def search():
    keyword = request.form.get('searched')
    results = Staff.query.filter(or_(Staff.surname.ilike(f'%{keyword}%'), Staff.firstname.ilike(f'%{keyword}%'))).all()
    print("--------")
    print(results)
    return render_template('search.html', results=results)

    # return jsonify([result.serialize() for result in results])






#staff get request.
@app.route('/staff', methods=['GET'])
def staff():
    staff=Staff.query.all()
    staffs = []
    print(staff)
    for st in staff:
        staffs.append({
            "surname":st.surname,
            "firstname":st.surname,
            "maiden_name":st.maiden_name,
            "offical_email":st.offical_email,
            "personal_email":st.personal_email,
            "position":st.position,
            "surname":st.surname,
            "member_staff":st.member_staff,
            "department_directorate_unit":st.department_directorate_unit,
            "number":st.number,
            "gender":st.gender,
            "position":st.position,
            "job_title":st.job_title,
            "employment_status":st.employment_status,
            "grade":st.grade,
        })
    print(staffs)
    return staffs





@app.route('/schools', methods=['GET', 'POST'])
def schools_view():
    if request.method == 'GET':
        responseArray = getallschools()
        print(responseArray)
        pprint.pprint(responseArray)
    return render_template('schools.html', response=responseArray)


@app.route('/api/v1/schools', methods=['GET', 'POST'])
def getallschools():
    if request.method == 'GET':
    # Handle the GET request to fetch all schools
        schools = School.query.order_by(School.id.desc()).all()
        schools_data = [{"name": school.name, "school": school.school,
                        "id":school.id,
                    "department": school.department, "program": school.program}
                for school in schools]
    # return schools_data
    elif request.method == 'POST':
        # Handle the POST request to add a new school
        body = request.get_json()
        new_school = School(name=body["name"], school=body["school"], department=body["department"], program=body["program"])
        db.session.add(new_school)
        db.session.commit()

        # Fetch all schools after the new one has been added
        post_schools = School.query.order_by(School.id.desc()).all()
        schools_data = [{"name": school.name,
                         "id":school.id, "school": school.school,
                        "department": school.department, "program": school.program}
                    for school in post_schools]

    return schools_data

#STUDENT UPDATE
@app.route('/api/v1/schools/<int:school_id>', methods=['PUT', 'DELETE'])
def update_school(school_id):
    if request.method == 'PUT':
        school = School.query.get(school_id)
        body = request.get_json()

        # Update the student's information with the provided data
        for key, value in body.items():
            setattr(school, key, value)
            
        # Commit the changes to the database
        db.session.commit()
        post_schools = School.query.order_by(School.id.desc()).all()
        schools_data = [{"name": school.name, "school": school.school,
                        "department": school.department, "program": school.program}
                    for school in post_schools]
        
    elif request.method == 'DELETE':
        school = School.query.get(school_id)
        db.session.delete(school)
        db.session.commit()
        post_schools = School.query.order_by(School.id.desc()).all()
        
        schools_data = [{"name": school.name, "school": school.school,
                            "department": school.department, "program": school.program}
                        for school in post_schools]

    return schools_data

# #school get request.
# @app.route('/school', methods=['GET', 'POST'])
# def school():
#     school=School.query.all()
#     schools = []
#     print(school)
#     for s in school:
#         schools.append({
#             "name":s.name,
#             "school":s.school,
#             "department":s.department,
#             "program":s.program
#         })
#     print("-------------")
#     print(schools)
#     print("-------------")
#     return schools



# #school post request.
# @app.route('/post_school', methods=['POST'])
# def post_school():
#     print(request.get_json())
#     body = request.get_json()
#     print(body)
#     print(body["name"],body["school"],body["department"],body["program"])
    
#     newschool = School(name=body["name"], school=body["school"],department=body["department"], program=body["program"])
    
#     db.session.add(newschool)
#     db.session.commit()
    
#     post_schools = School.query.all()
#      # Convert the School objects to a list of dictionaries (JSON serializable)
#     schools_data = [{"name": school.name, "school": school.school,
#                         "department": school.department, "program": school.program}
#                     for school in post_schools]
    
#     response_body = {
#         "data":post_school
#     }
#     return schools_data

@app.route('/departments', methods=['GET', 'POST'])
def department_view():
    if request.method == 'GET':
        responseArray = getalldepartments()
        print(responseArray)
        pprint.pprint(responseArray)
    return render_template('departments.html', response=responseArray)
   
@app.route("/api/v1/departments", methods=['GET', 'POST'])
def getalldepartments():
    if request.method == 'GET':
        departments = Department.query.order_by(Department.id.desc()).all()
        departments_data = [{
            "id": department.id,
            "name": department.name,
            "department": department.department,
            "school": department.school,
            "program": department.program
        } for department in departments]
        #return jsonify(departments_data)
    
    elif request.method == 'POST':
        body = request.get_json()
        new_department = Department(
            name=body["name"],
            school=body["school"],
            department=body["department"],
            program=body["program"]
        )
        db.session.add(new_department)
        db.session.commit()
        post_department = Department.query.order_by(Department.id.desc()).all()
    
        # Convert the School objects to a list of dictionaries (JSON serializable)
        departments_data = [{"name": department.name, 
                            "school": department.school,
                            "department": department.department,
                            "program": department.program}
                        for department in post_department]

    return departments_data
        
       
    
@app.route('/api/v1/departments/<int:department_id>', methods=['PUT', 'DELETE'])
def update_department(department_id):
    if request.method == 'PUT':
        department = Department.query.get(department_id)
        if not department:
            return jsonify({'error': f'Department with ID #{department_id} not found.'}), 404

        body = request.get_json()
        for key, value in body.items():
            setattr(department, key, value)

        db.session.commit()
        post_department = Department.query.order_by(Department.id.desc()).all()
        
        # Convert the School objects to a list of dictionaries (JSON serializable)
        departments_data = [{"name": department.name, 
                             "id":department.id,
                            "school": department.school,
                            "department": department.department,
                            "program": department.program}
                        for department in post_department]
    elif request.method == 'DELETE':
        department = Department.query.get(department_id)

        db.session.delete(department)
        db.session.commit()
        post_department = Department.query.all()
        
        # Convert the School objects to a list of dictionaries (JSON serializable)
        departments_data = [{"name": department.name, 
                             "id":department.id,
                            "school": department.school,
                            "department": department.department,
                            "program": department.program}
                        for department in post_department]

    return departments_data




@app.route('/students', methods=['GET', 'POST'])
def students_view():
    if request.method == 'GET':
        responseArray = getallstudents()
        print(responseArray)
        pprint.pprint(responseArray)
    return render_template('students.html', response=responseArray)
   
@app.route("/api/v1/students", methods=['GET', 'POST'])
def getallstudents():
    if request.method == 'GET':
        students = Student.query.order_by(Student.id.desc()).all()
        students_data = [{
                            "name": student.name, 
                            "school": student.school,
                            "id": student.id,
                            "department": student.department,
                            "program": student.program,
                            "email":student.email,
                            "password":student.password,
                            "telephone":student.telephone,
                            "bio":student.bio,
                            "current_company":student.current_company,
                            "socials":student.socials
        } for student in students]
    elif request.method == 'POST':
        body = request.get_json()
        new_student = Student(name=body["name"],
                              school=body["school"],
                              department=body["department"],
                              program=body["program"],
                              telephone=body['telephone'],
                              password=body['password'],
                              email=body['email'],
                              bio=body.get('bio', ""),
                              current_company=body.get('current_company', ""),
                              socials=body.get('socials', ""))
        db.session.add(new_student)
        db.session.commit()
        post_student = Student.query.order_by(Student.id.desc()).all()
        
        # Convert the School objects to a list of dictionaries (JSON serializable)
        students_data = [{"name": student.name, 
                            "school": student.school,
                            "id": student.id,
                            "department": student.department,
                            "program": student.program,
                            "email":student.email,
                            "password":student.password,
                            "telephone":student.telephone,
                            "bio":student.bio,
                            "current_company":student.current_company,
                            "socials":student.socials}
                        for student in post_student]
    return students_data
        
          
    
#STUDENT UPDATE
@app.route('/api/v1/students/<int:student_id>', methods=['PUT','DELETE'])
def update_students(student_id):
    if request.method == "PUT":
        # Fetch the student record by ID
        student = Student.query.get(student_id)
        body = request.get_json()
        # Update the student's information with the provided data
        for key, value in body.items():
            setattr(student, key, value)
            
        # Commit the changes to the database
        db.session.commit()
       
        post_student = Student.query.order_by(Student.id.desc()).all()
        
        students_data = [{"name": student.name, 
                          "id":student.id,
                            "school": student.school,
                            "department": student.department,
                            "program": student.program,
                            "email":student.email,
                            "password":student.password,
                            "telephone":student.telephone,
                            "bio":student.bio,
                            "current_company":student.current_company,
                            "socials":student.socials}
                        for student in post_student]
    elif request.method == 'DELETE':
        student = Student.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
 
        post_student = Student.query.order_by(Student.id.desc()).all()
        
        # Convert the School objects to a list of dictionaries (JSON serializable)
        students_data = [{"name": student.name, 
                            "school": student.school,
                            "id": student.id,
                            "department": student.department,
                            "program": student.program,
                            "email":student.email,
                            "password":student.password,
                            "telephone":student.telephone,
                            "bio":student.bio,
                            "current_company":student.current_company,
                            "socials":student.socials}
                        for student in post_student]
        
    return students_data








@app.route("/years", methods=['GET', 'POST'])
def year():
    if request.method == 'GET':
        years = Year.query.order_by(Year.id.desc()).all()
        years_data = [{
                            "name": year.name, 
                            "id":year.id,
                            "total":year.total
        } for year in years]
        return jsonify(years_data)
    
    elif request.method == 'POST':
            body = request.get_json()
            year_new = Year(name=body["name"],
                                total=body["total"],
            )
            db.session.add(year_new)
            db.session.commit()
            post_year = Year.query.order_by(Year.id.desc()).all()
            
            years_data = [{"name": year.name, 
                           "id":year.id,
                                "total": year.total,
                                }
                            for year in post_year]
            
            # response_body = {
            #     "data":post_student
            # }
            return jsonify(years_data)

  
#STUDENT UPDATE
@app.route('/years/<int:year_id>', methods=['PUT'])
def update_years(year_id):
    #try:
        # Fetch the student record by ID
        year = Year.query.get(year_id)
        body = request.get_json()
        # Update the student's information with the provided data
        for key, value in body.items():
            setattr(year, key, value)
            
        # Commit the changes to the database
        db.session.commit()
       
        post_year = Year.query.order_by(Year.id.desc()).all()
        
        year_data = [{"name": year.name, 
                           "id":year.id,
                                "total": year.total,}
                        for year in post_year]
        return jsonify(year_data)

#STUDENT DELETE
@app.route('/years/<int:year_id>', methods=['DELETE'])
def delete_years(year_id):
        year = Year.query.get(year_id)
        db.session.delete(year)
        db.session.commit()
 
        post_year = Year.query.order_by(Year.id.desc()).all()
        
        # Convert the School objects to a list of dictionaries (JSON serializable)
        year_data = [{"name": year.name, 
                           "id":year.id,
                                "total": year.total,}
                        for year in post_year]
        
        return jsonify(year_data)









if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
