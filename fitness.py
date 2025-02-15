import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Image and ImageTk

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
        summary = "Fitness Summary Report:\n\n"
        summary += "Workouts Log:\n"
        for workout in self.workouts:
            summary += workout.display_workout() + "\n"

        summary += "\nMeals Log:\n"
        for meal in self.meals:
            summary += meal.display_meal() + "\n"

        summary += "\nProgress Log:\n"
        for progress in self.progress_records:
            summary += progress.display_progress() + "\n"

        return summary


class FitnessTrackerGUI:
    def __init__(self, root):
        self.fitness_tracker = FitnessTracker()
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Load the image (initial size)
        self.bg_image = Image.open("smartphone-near-dumbbells.jpg")
        self.bg_image_tk = self.get_resized_image()

        # Create the Label widget with the image
        self.bg_label = tk.Label(root, image=self.bg_image_tk)
        self.bg_label.place(relwidth=1, relheight=1)

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        # Title Label
        self.label = tk.Label(self.frame, text="Personal Fitness Tracker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Workout Entry Fields
        self.workout_label = tk.Label(self.frame, text="Log Workout", font=("Helvetica", 12), bg="#f0f0f0")
        self.workout_label.pack(anchor="w", pady=5)
        
        self.exercise_name_label = tk.Label(self.frame, text="Exercise Name:", bg="#f0f0f0")
        self.exercise_name_label.pack(anchor="w")
        self.exercise_name_entry = tk.Entry(self.frame, width=40)
        self.exercise_name_entry.pack(pady=5)

        self.duration_label = tk.Label(self.frame, text="Duration (minutes):", bg="#f0f0f0")
        self.duration_label.pack(anchor="w")
        self.duration_entry = tk.Entry(self.frame, width=40)
        self.duration_entry.pack(pady=5)

        self.calories_label = tk.Label(self.frame, text="Calories Burned:", bg="#f0f0f0")
        self.calories_label.pack(anchor="w")
        self.calories_entry = tk.Entry(self.frame, width=40)
        self.calories_entry.pack(pady=5)

        self.add_workout_btn = tk.Button(self.frame, text="Add Workout", command=self.add_workout, bg="#4CAF50", fg="white")
        self.add_workout_btn.pack(pady=10)

        # Meal Entry Fields
        self.meal_label = tk.Label(self.frame, text="Log Meal", font=("Helvetica", 12), bg="#f0f0f0")
        self.meal_label.pack(anchor="w", pady=5)

        self.meal_name_label = tk.Label(self.frame, text="Meal Name:", bg="#f0f0f0")
        self.meal_name_label.pack(anchor="w")
        self.meal_name_entry = tk.Entry(self.frame, width=40)
        self.meal_name_entry.pack(pady=5)

        self.calories_meal_label = tk.Label(self.frame, text="Calories Consumed:", bg="#f0f0f0")
        self.calories_meal_label.pack(anchor="w")
        self.calories_meal_entry = tk.Entry(self.frame, width=40)
        self.calories_meal_entry.pack(pady=5)

        self.add_meal_btn = tk.Button(self.frame, text="Add Meal", command=self.add_meal, bg="#FF9800", fg="white")
        self.add_meal_btn.pack(pady=10)

        # Progress Entry Fields
        self.progress_label = tk.Label(self.frame, text="Log Progress", font=("Helvetica", 12), bg="#f0f0f0")
        self.progress_label.pack(anchor="w", pady=5)

        self.weight_label = tk.Label(self.frame, text="Weight (kg):", bg="#f0f0f0")
        self.weight_label.pack(anchor="w")
        self.weight_entry = tk.Entry(self.frame, width=40)
        self.weight_entry.pack(pady=5)

        self.body_fat_label = tk.Label(self.frame, text="Body Fat Percentage (%):", bg="#f0f0f0")
        self.body_fat_label.pack(anchor="w")
        self.body_fat_entry = tk.Entry(self.frame, width=40)
        self.body_fat_entry.pack(pady=5)

        self.add_progress_btn = tk.Button(self.frame, text="Add Progress", command=self.add_progress, bg="#2196F3", fg="white")
        self.add_progress_btn.pack(pady=10)

        # Display Summary Button
        self.display_summary_btn = tk.Button(self.frame, text="Display Summary", command=self.display_summary, bg="#9C27B0", fg="white")
        self.display_summary_btn.pack(pady=10)

        # Textbox to display summary
        self.summary_text = tk.Text(self.frame, width=60, height=10)
        self.summary_text.pack(pady=10)

        # Bind the resizing event to resize the background image
        self.root.bind("<Configure>", self.resize_bg_image)

    def get_resized_image(self):
        """Resizes the background image based on the window size."""
        width, height = self.root.winfo_width(), self.root.winfo_height()
        resized_image = self.bg_image.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def resize_bg_image(self, event):
        """Resizes the background image when the window size changes."""
        self.bg_image_tk = self.get_resized_image()
        self.bg_label.config(image=self.bg_image_tk)

    def add_workout(self):
        try:
            exercise_name = self.exercise_name_entry.get()
            duration = int(self.duration_entry.get())
            calories = int(self.calories_entry.get())
            workout = Workout(exercise_name, duration, calories)
            self.fitness_tracker.log_workout(workout)
            messagebox.showinfo("Success", f"Workout '{exercise_name}' logged!")
            self.clear_workout_entries()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for duration and calories.")

    def add_meal(self):
        try:
            meal_name = self.meal_name_entry.get()
            calories = int(self.calories_meal_entry.get())
            meal = Meal(meal_name, calories)
            self.fitness_tracker.log_meal(meal)
            messagebox.showinfo("Success", f"Meal '{meal_name}' logged!")
            self.clear_meal_entries()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for calories.")

    def add_progress(self):
        try:
            weight = float(self.weight_entry.get())
            body_fat = float(self.body_fat_entry.get())
            progress = Progress(weight, body_fat)
            self.fitness_tracker.log_progress(progress)
            messagebox.showinfo("Success", "Progress logged!")
            self.clear_progress_entries()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for weight and body fat.")

    def display_summary(self):
        summary = self.fitness_tracker.display_summary()
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

    def clear_workout_entries(self):
        self.exercise_name_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.calories_entry.delete(0, tk.END)

    def clear_meal_entries(self):
        self.meal_name_entry.delete(0, tk.END)
        self.calories_meal_entry.delete(0, tk.END)

    def clear_progress_entries(self):
        self.weight_entry.delete(0, tk.END)
        self.body_fat_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = FitnessTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
