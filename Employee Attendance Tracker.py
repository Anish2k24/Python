import pandas as pd
import numpy as np

num_employees = 30   
employee_info = {
    "employee_id": [f"U{str(i).zfill(3)}" for i in range(1, num_employees + 1)],
    "employee_name": [f"emp_{i}" for i in range(1, num_employees + 1)],
    "roll_number": [f"R{str(i).zfill(3)}" for i in range(1, num_employees + 1)]
}

employee_data = pd.DataFrame(employee_info)
print("\nEmployee List:")
print(employee_data)

np.random.seed(42)
total_working_days = 45 

attendance_records = {"employee_id": np.arange(1, num_employees + 1)}
for day in range(1, total_working_days + 1):
    attendance_records[f"day_{day}"] = np.random.choice(["p", "a"], num_employees) 

attendance_data = pd.DataFrame(attendance_records)

def calculate_attendance_summary(attendance_df):
    attendance_df["present_days"] = np.sum(attendance_df.iloc[:, 1:] == "p", axis=1)
    attendance_df["absent_days"] = np.sum(attendance_df.iloc[:, 1:] == "a", axis=1)
    return attendance_df

attendance_data = calculate_attendance_summary(attendance_data)

print("\nAttendance Summary:")
print(attendance_data[["employee_id", "present_days", "absent_days"]])

def calculate_attendance_percentage(attended, total):
    return (attended / total) * 100 if total != 0 else 0

default_attended_days = 30
default_attendance_percentage = calculate_attendance_percentage(default_attended_days, total_working_days)
print(f"\nDefault Attendance Percentage: {default_attendance_percentage:.2f}%")

attended_days = int(input("Enter attended days: "))
working_days = int(input("Enter total working days: "))
user_attendance_percentage = calculate_attendance_percentage(attended_days, working_days)
print(f"User Attendance Percentage: {user_attendance_percentage:.2f}%")

def generate_attendance_report(attendance_df):
    for _, row in attendance_df.iterrows():
        print(f"\nEmployee ID: {row['employee_id']} - Present: {row['present_days']} days, Absent: {row['absent_days']} days")

print("\nAttendance Report:")
generate_attendance_report(attendance_data)

updated_attendance_data = attendance_data.copy()
updated_attendance_data["leave_days"] = total_working_days - (updated_attendance_data["present_days"] + updated_attendance_data["absent_days"])
print("\nUpdated Attendance Report with Leave Days:")
print(updated_attendance_data[["employee_id", "present_days", "absent_days", "leave_days"]])
