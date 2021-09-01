
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lalebdi/FlaskIncreaseSalary">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Increase Salary</h3>

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#link">Link</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This is a Flask API in a docker image.



* :smile:



### Built With


* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask_restful](https://flask-restful.readthedocs.io/en/latest/)
* [docker](https://www.docker.com/)



<!-- GETTING STARTED -->
## Getting Started


To get a local copy up and running follow these simple example steps.

### Prerequisites

This is how to setup the software you need to use and how to install them.
* Docker
  [https://www.docker.com/](https://www.docker.com/) 

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/lalebdi/FlaskIncreaseSalary.git
   cd FlaskIncreaseSalary
   ```
  
2. Build
   ```sh
   docker build -t increase_salary:latest .    
   ```
3. Run the container
   ```sh
    docker run -it -p 5000:5000  increase_salary      
   ```


Your API is running on  http://localhost:5000/

<!-- USAGE EXAMPLES -->
## Usage

This URL will accept PUT and GET requests:

* GET http://localhost:5000/ : will list all the employees.
* PUT http://localhost:5000/ : Error message. 
* GET  http://localhost:5000/tony : will display Tony's name and salary
* PUT  http://localhost:5000/tony : will increase Tony's salary 5%
* GET  http://localhost:5000/steve : will display Steve's name and salary
* PUT  http://localhost:5000/steve : will increase Steve's salary 5%
* GET  http://localhost:5000/bruce : will display Bruce's name and salary
* PUT  http://localhost:5000/bruce : will increase Bruce's salary 5%


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

This is a private project and usage of anything in the project is prohibited.



<!-- CONTACT -->
## Contact

lalebdi - [https://www.leahwebdev.com](https://www.leahwebdev.com) 

Project Link: [https://github.com/lalebdi/FlaskIncreaseSalary](https://github.com/lalebdi/FlaskIncreaseSalary)

