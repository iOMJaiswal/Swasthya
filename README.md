# Swasthya - Health Emergency Web-App

Swasthya is a Health Emergency Web-App that aims to merge all health-related emergency applications into one user-friendly and responsive platform. The word "Swasthya" originates from Sanskrit, meaning "Health". This project is built using Django and Bootstrap frameworks, along with Python, HTML/CSS, and Javascript languages. The database used for this application is Sqlite3, and the security features are powered by the Django Authentication System.

## Project Description

The primary objective of Swasthya is to provide a seamless experience for users during health emergencies. The web application is designed with simplicity and user-friendliness in mind, offering a responsive design that adapts to various devices.

### Key Modules

Swasthya incorporates various modules to cater to different health emergency needs:

1. **First Aid**:
   - Users can access a comprehensive list of first aid procedures for different health problems.
   - Additionally, authenticated users can contribute to the list by adding new first aid procedures.

2. **Order Ambulance**:
   - In case of an emergency, users can request an ambulance with just two clicks.
   - The web-app utilizes the user's live location to send an ambulance request based on the urgency of the situation.

3. **Make Appointment**:
   - Users can search for doctors and view their respective hospitals, degrees, and contact information.
   - Authenticated users can also book appointments with doctors conveniently through the web-app.

## Additional Features

Swasthya offers additional features that require users to log in to the application:

- **Add First Aids**:
  - Authenticated users have the privilege to contribute to the list of first aid procedures, enriching the emergency resources available to others.

- **Add New Doctor**:
  - Users with appropriate permissions can add new doctors to the platform along with their relevant details, enhancing the database of available healthcare providers.

- **Book Appointments**:
  - Authenticated users can book appointments with doctors effortlessly, ensuring timely access to healthcare services.

## Installation and Setup

Follow these steps to set up the Swasthya project on your local machine:

1. Clone the repository:

```bash
git clone https://github.com/iOMJaiswal/Swasthya.git
```

2. Change into the project directory:

```bash
cd Swasthya
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the migrations:

```bash
python manage.py migrate
```

5. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Access the web-app locally:

Open your web browser and go to `http://localhost:8000/`

## Contribute

We welcome contributions to enhance the Swasthya project and make it even more valuable for users in emergencies. If you have any feature suggestions, bug reports, or code improvements, please feel free to submit a pull request or create an issue in the repository.


Thank you for your interest in Swasthya! We hope this web application serves its purpose of providing critical health emergency services at your fingertips. If you have any questions or need further assistance, please don't hesitate to reach out. Happy coding!
