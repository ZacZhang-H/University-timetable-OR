# Operational research for University timetable
Topics in Applied OR Project. 

Detail report can see document "Timetabling Optimization Project for the School of Mathematics"

# Timetabling Optimization Project for the School of Mathematics

## Introduction
This project aims to optimize university-level timetables through a blend of Mixed Integer Programming (MIP) models and sophisticated optimization algorithms, tackling various scheduling constraints. It leverages datasets containing course information, student enrollment numbers, and room capacities, all undergoing thorough preprocessing for precision and applicability.

## Team Members
- Haoyuan Zhang
- Yuxin Li
- Yuting Zhang
- Anagha Indulal Nair

## Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
    - [Timetable for Lectures](#timetable-for-lectures)
    - [Timetable for Workshops](#timetable-for-workshops)
- [Conclusion and Suggestions](#conclusion-and-suggestions)
- [Data Preprocessing](#data-preprocessing)
- [Explanation for Constraints](#explanation-for-constraints)
- [PSO Functions](#pso-functions)
- [Results and Figures](#results-and-figures)
- [Code](#code)
- [Further Improvements](#further-improvements)
- [References](#references)
## Introduction
The optimization of university schedules is crucial for the seamless operation of educational institutions.  This report explores the intricate task of optimizing university-level timetables through a blend of Mixed Integer Programming (MIP) models and sophisticated optimization algorithms to tackle a variety of scheduling constraints.  Our analysis is grounded in a dataset comprising detailed course information, student enrollment numbers, and room capacities, all of which undergo thorough preprocessing to guarantee precision and applicability.

Our methodology leverages an innovative amalgamation of algorithms designed to adeptly navigate both hard and soft constraints, crafting a schedule that is both realistic and efficient.  Given the pivotal role of lectures and workshops in the academic schedule, our optimisation process is bifurcated into two distinct models: one for optimising lectures and another for workshops.  This division allows for targeted consideration of specific constraints such as room capacity, class timing without overlaps, and the need for lecture recording facilities.  Our primary objective is to minimise both the incidence and quantity of course conflicts.  To this end, we employ Particle Swarm Optimization and Simulated Annealing algorithms for the lecture model, applying these to a preliminarily generated timetable to effectively reduce course conflicts.

Conversely, the workshop model focuses on accommodating multiple sessions within constrained classroom capacities, enabling students to select class times that best suit their schedules.  This aims to decrease the overall frequency of instructional sessions, thereby alleviating the workload on faculty and staff.  Here, we predominantly utilise Genetic Algorithms, iterating through numerous mutations to meet our optimisation targets.

Remarkably, our strategy has proven both successful and replicable.  We have managed to decrease the number of scheduling conflicts from 25 to 8 and reduce the courses involved in conflicts from 39 to 21. For the workshop, we reduced the total number of classes from 361 to 182, demonstrating the efficacy of our approach in enhancing the scheduling framework of university timetables.
## Methodology
Detailed explanations of algorithms used, including Simulated Annealing, Particle Swarm Optimization Algorithm, and Genetic Algorithm, highlighting their application to both lectures and workshops timetabling.

### Timetable for Lectures
Describes the initial generation and optimization of lecture timetables using Particle Swarm Optimization and Simulated Annealing algorithms.

### Timetable for Workshops
Focuses on the setup and optimization of workshop timetables using Genetic Algorithms, addressing the challenge of scheduling multiple sessions within constrained classroom capacities.

## Conclusion and Suggestions
Summarizes the project's achievements in reducing scheduling conflicts and courses involved in conflicts. Offers further improvements for the school based on the project findings.

## Data Preprocessing
Outlines the preprocessing steps taken for data cleaning and organization, preparing it for effective optimization.

## Explanation for Constraints
Provides a detailed explanation of the constraints applied in the Mixed Integer Programming Model for timetabling.

## PSO Functions
Explains the specific functions used in the Particle Swarm Optimization algorithm, detailing the optimization process.

## Results and Figures
Includes figures and results from the application of optimization algorithms to both lectures and workshops, demonstrating the efficacy of the approaches.

## Code
Access the project's full code repository on GitHub: [University Timetable OR Project](https://github.com/ZacZhang-H/University-timetable-OR.git)

## Further Improvements
Discusses potential enhancements and areas of focus for further development of the timetabling optimization project.

## References
A list of all references used in the development and documentation of the project.

---

For more information or to contribute to the project, please contact [Haoyuan Zhang](mailto:example@example.com).

