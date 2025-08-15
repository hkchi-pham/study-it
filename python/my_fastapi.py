from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Minh Van",
        "age": 16,
        "class": "Year 12"
    },
    2:{
        "name": "Khanh Chi",
        "age": 15,
        "class": "Year 12"
    }
}

# create new api endpoint
@app.get("/")
def index():
    return {"name": "First Data"}

#path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view",gt=0,lt=3)):
    return students[student_id]

#query parameter