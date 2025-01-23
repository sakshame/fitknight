# FitKnight - Fitness App

FitKnight is a fitness application designed to help users manage their fitness routines, connect with fitness groups, and track their progress. The app is built using **React** for the frontend and **Django** with **SQLite** for the backend.

---

## Features

- **Fitness Groups**: Join and interact with fitness groups to stay motivated.
- **Locations**: Find nearby fitness centers or outdoor locations for workouts.
- **Messaging**: Communicate with other users or group members.
- **User Profiles**: Create and manage your fitness profile.
- **Progress Tracking**: Track your fitness progress over time.

---

## Technologies Used

### Frontend
- **React**: A JavaScript library for building user interfaces.
- **CSS**: For styling the components and making the app visually appealing.

### Backend
- **Django**: A high-level Python web framework for building robust backend systems.
- **SQLite**: A lightweight, serverless database used for local development.

---

## Installation

### Prerequisites
- Node.js (for React frontend)
- Python 3.x (for Django backend)
- pip (Python package manager)

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sakshame/fitknight.git
   cd fitknight
   ```

2. **Set Up the Backend**
   - Navigate to the `fitness_backend` directory:
     ```bash
     cd fitness_backend
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

3. **Set Up the Frontend**
   - Navigate to the `fitness_frontend` directory:
     ```bash
     cd ../fitness_frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

4. **Access the Application**
   - The React app will be running on `http://localhost:3000`.
   - The Django backend will be running on `http://localhost:8000`.

---

## Project Structure

### Backend (`fitness_backend`)
- `manage.py`: Django's command-line utility for administrative tasks.
- `settings.py`: Django project settings.
- `urls.py`: URL routing for the backend.
- `models.py`: Database models for fitness groups, locations, and messages.
- `views.py`: Backend logic and API endpoints.
- `serializers.py`: Serializers for converting data to JSON.

### Frontend (`fitness_frontend`)
- `src/`: Contains the React application code.
  - `components/`: Reusable React components (e.g., `FitnessGroupList`, `LocationList`, `MessageList`).
  - `App.js`: Main application component.
  - `App.css`: Styles for the application.
  - `index.js`: Entry point for the React app.
  - `index.css`: Global styles.

---

## API Endpoints

### Fitness Groups
- `GET /api/fitness-groups/`: Fetch all fitness groups.
- `POST /api/fitness-groups/`: Create a new fitness group.

### Locations
- `GET /api/locations/`: Fetch all locations.
- `POST /api/locations/`: Add a new location.

### Messages
- `GET /api/messages/`: Fetch all messages.
- `POST /api/messages/`: Send a new message.
---

## Contributing

We welcome contributions! If you'd like to contribute to FitKnight, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch to your forked repository.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Saksham**  
  Email: saksham@example.com  
  GitHub: [sakshame](https://github.com/sakshame)

---

Thank you for using FitKnight! Stay fit and healthy! 💪
