import streamlit as st

# ----- Class Definitions -----

class Workout:
    def __init__(self, exercise_name, duration_minutes, calories_burned):
        self.exercise_name = exercise_name
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned

    def display_workout(self):
        return f"Exercise: {self.exercise_name}, Duration: {self.duration_minutes} min, Calories Burned: {self.calories_burned} kcal"

class Meal:
    def __init__(self, meal_name, calories_consumed):
        self.meal_name = meal_name
        self.calories_consumed = calories_consumed

    def display_meal(self):
        return f"Meal: {self.meal_name}, Calories Consumed: {self.calories_consumed} kcal"

class Progress:
    def __init__(self, weight, body_fat_percentage):
        self.weight = weight
        self.body_fat_percentage = body_fat_percentage

    def display_progress(self):
        return f"Weight: {self.weight} kg, Body Fat: {self.body_fat_percentage}%"

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.meals = []
        self.progress_records = []

    def log_workout(self, workout):
        self.workouts.append(workout)

    def log_meal(self, meal):
        self.meals.append(meal)

    def log_progress(self, progress):
        self.progress_records.append(progress)

    def display_summary(self):
        summary = "### 📝 Fitness Summary Report\n"
        
        summary += "\n**🏋️ Workouts Log:**\n"
        if self.workouts:
            for workout in self.workouts:
                summary += f"- {workout.display_workout()}\n"
        else:
            summary += "- No workouts logged.\n"

        summary += "\n**🍱 Meals Log:**\n"
        if self.meals:
            for meal in self.meals:
                summary += f"- {meal.display_meal()}\n"
        else:
            summary += "- No meals logged.\n"

        summary += "\n**📊 Progress Log:**\n"
        if self.progress_records:
            for progress in self.progress_records:
                summary += f"- {progress.display_progress()}\n"
        else:
            summary += "- No progress recorded.\n"

        return summary


# ----- Main App -----
st.set_page_config(page_title="Fitness Tracker", layout="wide")
st.title("💪 Personal Fitness Tracker")

# Session state
if 'tracker' not in st.session_state:
    st.session_state.tracker = FitnessTracker()

tracker = st.session_state.tracker

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Log Workout", "Log Meal", "Log Progress", "View Summary"])

# Log Workout
if menu == "Log Workout":
    st.header("🏋️ Log Workout")
    with st.form("workout_form"):
        exercise = st.text_input("Exercise Name")
        duration = st.number_input("Duration (minutes)", min_value=0)
        calories = st.number_input("Calories Burned", min_value=0)
        submitted = st.form_submit_button("Add Workout")
        if submitted:
            workout = Workout(exercise, duration, calories)
            tracker.log_workout(workout)
            st.success(f"✅ Workout '{exercise}' logged!")

# Log Meal
elif menu == "Log Meal":
    st.header("🍱 Log Meal")
    with st.form("meal_form"):
        meal_name = st.text_input("Meal Name")
        meal_calories = st.number_input("Calories Consumed", min_value=0)
        submitted = st.form_submit_button("Add Meal")
        if submitted:
            meal = Meal(meal_name, meal_calories)
            tracker.log_meal(meal)
            st.success(f"✅ Meal '{meal_name}' logged!")

# Log Progress
elif menu == "Log Progress":
    st.header("📊 Log Progress")
    with st.form("progress_form"):
        weight = st.number_input("Weight (kg)", min_value=0.0)
        body_fat = st.number_input("Body Fat Percentage (%)", min_value=0.0)
        submitted = st.form_submit_button("Add Progress")
        if submitted:
            progress = Progress(weight, body_fat)
            tracker.log_progress(progress)
            st.success("✅ Progress logged!")

# Display Summary
elif menu == "View Summary":
    st.header("📋 Fitness Summary")
    summary_text = tracker.display_summary()
    st.markdown(summary_text)
