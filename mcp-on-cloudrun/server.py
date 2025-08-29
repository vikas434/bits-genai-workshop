import asyncio
import logging
import os
import httpx
from typing import List, Dict, Any

from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("Bits MCP Server 🦁🐧🐻")

# Dictionary of animals at the zoo
'''
ZOO_ANIMALS = [
    {
        "species": "lion",
        "name": "Leo",
        "age": 7,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "Nala",
        "age": 6,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "Simba",
        "age": 3,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "King",
        "age": 8,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "penguin",
        "name": "Waddles",
        "age": 2,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Pip",
        "age": 4,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Skipper",
        "age": 5,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Chilly",
        "age": 3,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Pingu",
        "age": 6,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Noot",
        "age": 1,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "elephant",
        "name": "Ellie",
        "age": 15,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Peanut",
        "age": 12,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Dumbo",
        "age": 5,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Trunkers",
        "age": 10,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "bear",
        "name": "Smokey",
        "age": 10,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Grizzly",
        "age": 8,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Barnaby",
        "age": 6,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Bruin",
        "age": 12,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "giraffe",
        "name": "Gerald",
        "age": 4,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Longneck",
        "age": 5,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Patches",
        "age": 3,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Stretch",
        "age": 6,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Speedy",
        "age": 2,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Dash",
        "age": 3,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Gazelle",
        "age": 4,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Swift",
        "age": 5,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "polar bear",
        "name": "Snowflake",
        "age": 7,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "polar bear",
        "name": "Blizzard",
        "age": 5,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "polar bear",
        "name": "Iceberg",
        "age": 9,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Wally",
        "age": 10,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Tusker",
        "age": 12,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Moby",
        "age": 8,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Flippers",
        "age": 9,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    }
]
'''
Second_Year_Guide = [
    {
  "metadata": {
    "title": "SU Study Guide for Sophomores",
    "authors": [
      "Kamal Chauhan",
      "Karande Ashirwad Abhiman"
    ],
    "date": "2021-2022",
    "keywords": [
      "Study Guide",
      "Sophomores",
      "Academics",
      "Engineering",
      "Science"
    ],
    "source": "Students' Union 21-22"
  },
  "sections": [
    {
      "heading": "INTRODUCTION",
      "subsections": [
        {
          "heading": None,
          "content": [
            {
              "type": "paragraph",
              "text": "This Study Guide is all that a second yearite would need to ace his academics in his/her 2nd year."
            },
            {
              "type": "paragraph",
              "text": "The Guide is a fully researched resource that documents how the best students from every stream planned and studied."
            },
            {
              "type": "paragraph",
              "text": "The IInd yearites can learn from these anecdotes which mistakes they need to avoid."
            },
            {
              "type": "paragraph",
              "text": "The Guide is the one document that these students need to refer to whenever they feel troubled by a course."
            },
            {
              "type": "paragraph",
              "text": "The IInd year is a very important year for all the students. Students from all disciplines get introduced to their core courses that lay the fundamentals of their future academic journey in college life."
            },
            {
              "type": "paragraph",
              "text": "It is very important that the students realize the correct set of steps and follow them to avoid the common mistakes and achieve their true academic potential."
            },
            {
              "type": "paragraph",
              "text": "The Guide aims to help the students with their academic journey in their IInd year."
            },
            {
              "type": "paragraph",
              "text": "Happy Learning!"
            }
          ]
        }
      ]
    },
    {
      "heading": "ACKNOWLEDGEMENT",
      "subsections": [
        {
          "heading": None,
          "content": [
            {
              "type": "paragraph",
              "text": "We would like to express our special thanks and gratitude to all the students who volunteered to contribute to this Study Guide."
            },
            {
              "type": "paragraph",
              "text": "We are aware that documenting their experiences and mistakes must have taken a lot of effort."
            },
            {
              "type": "paragraph",
              "text": "We hope that the Guide can help all the IInd yearites with their doubts regarding their courses."
            },
            {
              "type": "paragraph",
              "text": "We have tried our best to cover all the areas required for the IInd yearites to excel academically."
            }
          ]
        }
      ]
    },
    {
      "heading": "A1: Chemical Engineering",
      "subsections": [
        {
          "heading": "By Sanjana Sunit Jamuar",
          "content": [
            {
              "type": "subsection",
              "heading": "Semester 1 Overview:",
              "content": [
                {
                  "type": "paragraph",
                  "text": "This being your first semester for your disciplinary course is important as it will be the base for all the subjects you'll be learning in the future semesters. Most of the subjects are an extension of what you've already learned in your 11th and 12th, you just need to be regular with classes. There'll be a lot of 8am tut tests, which are easy to solve if you've done the examples in lectures and textbooks. This is an important semester in terms of your CGPA as for PS I this CGPA will be considered while allocating you stations and trust me there are only a few reputed stations where you'll learn a lot and will be helpful for your CV."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F211, Chemical process calculations",
              "content": [
                {
                  "type": "paragraph",
                  "text": "The course is based on the principles of mass balance. You should be clear on the law of conservation of mass. This course becomes boring as soon as it starts, but it can be tricky to apply the logic as they have been taught in the class during your exams."
                },
                {
                  "type": "bullet_list",
                  "items": [
                    "Attend classes and tutorials regularly, you'll have a lot of tut tests in this subject, 6-7 spread through the semester so try and keep up with the classes.",
                    "Practice questions done during lectures and tutorials to solidify your concepts.",
                    "Examples from textbook, lecture material are the ideal resources to study.",
                    "Strict grading, try and score as many marks in the tut tests as the mid sems and compres are lengthy and tricky to solve.",
                    "Take inputs from the lecturer on how to do the assignments to score extra marks."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F212, Fluid Mechanics",
              "content": [
                {
                  "type": "paragraph",
                  "text": "This course is the basic introduction to fluid mechanics, covering the fundamental and practical aspects of fluid flow. It is an important technical subject which will be taken up during interviews if you opt for Core Chemical Sls. Also, a prerequisite for Chemical Lab-l which will come up during your 3-1. The recommended textbook (Fox, R.W. and A.T. McDonalds, Introduction to Fluid Mechanics (8th Ed.), John Wiley & Sons Inc., 2011.) is great, has good explanations for concepts and examples accompanying this. Dr, Pratik N Sheth was my instructor and his classes can be a little slow at times but you are recommended to go to lectures because he gives out problems during lecture hours which helps you understand the concepts and also, ace the tutorial tests."
                },
                {
                  "type": "bullet_list",
                  "items": [
                    "Lectures and tutorial hours are a must attend. There are 7 surprise tut tests out of which 6 are counted. These are open/closed books which are announced during the tut hour. It is easier to score for the tut tests as the aggregated average is generally low and you can score well above the average at the end of the semester.",
                    "Mid-sem and Compre have both open and closed book tests and for which I recommend to brush up the examples and basics, the questions for the closed book tests can be direct and concept based whereas, for the open book you have to be thorough with practice.",
                    "Grading is good, in a class of 120 students about 14 students got A grade.",
                    "Average + 6-8 helps you get a B-."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F213, Chemical Engineering Thermodynamics",
              "content": [
                {
                  "type": "paragraph",
                  "text": "This course involves the application of the first and second laws of thermodynamics, basics that you've learned in Thermodynamics in your first year. Applications of work, heat, reversible and irreversible processes. Equation of states, generalized correlation for the PVT behavior. A lot of new and important concepts like the Maxwell relations, fluid property estimations, Gibbs-Duhem equation and Vapor Liquid Equilibria are introduced."
                },
                {
                  "type": "bullet_list",
                  "items": [
                    "We had lectures as well as tutorial tests. The lectures are fast paced but don't rush through the syllabus. The advantages of attending lectures is that it helps you cover most of the syllabus for the tutorial tests as you'll only have to practice examples given in the textbook. Although most of the content taught in the lecture is straight out of the textbook, it takes time to understand the basic concepts which are important if you are looking for a Core job as this is one of the important subjects.",
                    "The recommended textbook (J. M. Smith,, H C Van Ness, M. M. Abbott and M. T. Swihart (Adapted by: B I Bhatt), Introduction to Chemical Engineering Thermodynamics (8th ed.), Tata McGraw Hill, special Indian Edition 2020.)is pretty much all you need to study. I would suggest all the examples from each of the chapters to be solved as the tut test questions as well as the open book questions in mid sem and compre are pretty straight forward. Mark the textbook well otherwise you'll be lost during open book exams.",
                    "Like in Fluid Mechanics, try attempting all the tut-tests as they push you well above average. Open book marking is purely final answer based, so make sure to complete the questions in mid-sem and compres. Keep in handy all the values of gas constant for the closed book tests.",
                    "A.K. Pani is an amazing teacher and will value you if you are regular in his classes."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F214, Engineering Chemistry",
              "content": [
                {
                  "type": "paragraph",
                  "text": "The course is about understanding the various developments in the field of water treatment, polymers, instrumental method of analysis, etc. The objective of the course is to study these areas in detail, and understand the important working principles of equipment involved. To score good marks in all the evaluations please attend lectures. The professor takes attendance very seriously and is partial towards people who attend classes. A lot of important material is taught during tutorial hours, so make sure you attend those. There are no surprise tests, all the tests will be announced beforehand. The recommended book (Vairam SRamesh SEngineering Chemistry, Wiley India, 2011) is very extensive, and lectures only cover like 45% of the material which is expected of you during examinations. There is a lot of material to learn because the course is completely closed book. Be regular with the reading of the textbook to not pile up just before exams. PYQs are important as they give an idea about important topics which you should focus on, like wastewater treatment is one of the most important topics. Strict checking and grading. Each word in your answer sheet will be evaluated for its relevance. To the point answers are expected. We also had an assignment which was evaluated on the basis of our knowledge of the topic and research work."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "MATH F211, Mathematics-III",
              "content": [
                {
                  "type": "paragraph",
                  "text": "This course is the study of differential equations with the introduction to solving boundary value problems using various classical methods. You have to have thorough knowledge of differential equations taught in calculus of +2."
                },
                {
                  "type": "bullet_list",
                  "items": [
                    "Attending lectures of Prof. Krishnendra Shekhawat, as along with basic concepts he gives out a lot of problems to solve during lecture hours which will make it easier to understand.",
                    "Solve suggested questions from the textbook and pyqs to help understand as well as learn the concepts. Make marked notes to make sure you don't waste your time skimming through the notes during open book exams.",
                    "It is a very high scoring subject and you need to really practice to know the type of questions asked and manage time efficiently during exams. 2 out of 3 tut tests are considered which again are very high scoring so try to remain above average at all times. A grade was given on Av+ 75."
                  ]
                }
              ]
            },
            {
              "type": "paragraph",
              "text": "Also, a general suggestion for this semester, try to gauge which subjects you can understand even without attending lectures if you are struggling to manage time along with your extracurricular activities. Don’t miss any of the tut tests to remain above average on your pre-compre total, as this will take off some pressure from the major exams. For huels, attend all the lectures, the teachers give out marks if they know your name and you are actively participating during lecture hours."
            },
            {
              "type": "subsection",
              "heading": "Semester 2 Overview:",
              "content": [
                {
                  "type": "paragraph",
                  "text": "After the first semester you understand how much effort you have to put in to score good in CDCs. You can also try some opels to gauge your interests towards certain minors like Finance, DS etc. You might have already gotten a reality check on Chemical, people might say it is one of the lighter branches but honestly, the number of tests we face is equal to that of any other branch. You are also given a choice between Principles of Economics and Principles of Management. If you want to pursue a finance minor,POE is the obvious choice, but overall the subject is really interesting and scoring. POM has lesser number of students, compared of POE."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F241, Heat Transfer",
              "content": [
                {
                  "type": "numbered_list",
                  "items": [
                    "The course is about the steady and unsteady state conduction, convection and radiation. It starts off with the basics of heat transfer due to conduction and convection that we’ve already learnt in class 12. Then the level increases with the introduction to fins and unsteady state convection. And then there will be many dimensionless numbers which will be in use like reynolds, grashoffs, nusselts, and it can be a little confusing at times.",
                    "Lectures can keep you updated for the tut tests and you will understand how to solve the problems. The lectures are based on books and you will be solving a lot of questions to help with the concepts. There’ll be 6 tut-tests out of which 4 will be considered and 2 assignments before mid sem and compre respectively",
                    "Understand the concepts using the recommended textbook (Holman, J.P., Bhattacharyya, S. (2011), “Heat Transfer”, 10th Ed., Tata McGraw Hill Education Pvt Ltd, New Delhi.), quick revision through slides, before mid sem and compre take the assignments seriously, similar questions are asked. Solve the given examples for practice and the questions covered during lecture hours. Give all the tutorial tests to stay well above average and take the pressure off mid sem and compre.",
                    "Good grading depending on the class strength about 10 % people get A. This is an important subject if you want to study Transport Phenomenon and Computational Fluid Dynamics. The concepts will also be used in Chem Lab I in your 3-1.",
                    "Don’t freak due to closed book tests as the questions asked are based on basic concepts taught in lectures. You don’t have to learn the bigger formulas, just the easy ones and know how to correlate the concepts."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F242, Numerical Methods for Chemical Engineering",
              "content": [
                {
                  "type": "numbered_list",
                  "items": [
                    "This is the introduction to mathematical modeling and engineering problem solving. It will help students to use numerical techniques to solve allergic and differential equations. Learning numerical methods for differentiation, integration and curve fitting, which helps us solve various problems of Chemical engineering subjects.",
                    "This course is all about problem solving and practice. Questions done during lecture hour, tutorial hour and PYQs. Try learning MATLAB along with this subject to get hold of the software as it is very important for chemical engineering.",
                    "The textbook (Chapra, S. C. and R. P. Canale, Numerical Methods for Engineers, 7th Edition, McGraw Hill Education (India) Pvt. Ltd., New Delhi, 2015) has a lot of problems to practice, tutorial hours are important as there are many surprise tests.",
                    "In a class of about 120 students 11-13 students get an A grade.",
                    "There is a lot to remember for the closed book test so make sure you are in regular practice to not get confused between the concepts."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F243, Material Science",
              "content": [
                {
                  "type": "numbered_list",
                  "items": [
                    "Introduction to various materials for engineering and their significant properties. You learn about metals, ceramics, polymers and composites. Corrosion of materials and the evolution of materials.",
                    "The book is easy to understand but the questions asked are seldom from the book. Questions practiced during tutorial hours are important and direct questions are asked in the exams. Attending lectures is completely up to you.",
                    "PYQs are important as the tests are mostly numerical with little to no theory asked.",
                    "Strict grading for tests and assignments. You won’t be allowed in the class if you are 5+ mins late."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "CHE F244, Separation Process I",
              "content": [
                {
                  "type": "numbered_list",
                  "items": [
                    "The most interesting subjects of 2-2. All you have to do is go to lectures, make notes and that’s it. It is about molecular diffusion in fluids, mass transfer, mass transfer coefficient and concepts involved in adsorption, stripping, distillation and liquid-liquid extraction. You’ll learn problem solving in the lectures and all the concepts are so well taught.",
                    "To study this subject all you need are the notes and understanding the art of graphical problem solving which will be taught during lecture hours.",
                    "Practice problems from assignments and PYQs, direct questions are asked in tut tests and mid sem compres.",
                    "Important prerequisites for Chemical Lab I and Separation Process II. The grading is linenet."
                  ]
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "ECON F211, Principles of Economics",
              "content": [
                {
                  "type": "numbered_list",
                  "items": [
                    "PoE is a foundation course that introduces us to the field of Economics and Finance. We are taught all the basics economics, micro and macro. It is an important course if you are thinking of pursuing a Finance Minor.",
                    "PYQs is the best way to study the subject as the questions asked during tut tests and mid sem compres are very similar and you just need to know the methodology of solving certain problems.",
                    "The recommended textbook is amazing, you get to learn everything through examples. If you find yourself not attending classes, I suggest you diligently read the textbook and keep up with the syllabus in order to not fall behind.",
                    "About 700-800 students take up this course so it has a better range for grading but a lot of students tend to take lite and since it’s a very scoring subject averages are very high so don’t fall below the average line because it awards you a C grade."
                  ]
                }
              ]
            },
            {
              "type": "paragraph",
              "text": "Overall, This year is going to be a rollercoaster ride. Don’t forget enjoying college life in lieu of studying all the time. Try and balance time as that will be the best life lesson from this year. Set your priorities straight and you'll find yourself in a comfortable place by the end of 2-2."
            },
            {
              "type": "paragraph",
              "text": "Written by:\nSanjana Sunit Jamuar\n2020A1PS0198P"
            }
          ]
        },
        {
          "heading": "By Arnav Singh",
          "content": [
            {
              "type": "subsection",
              "heading": "Semester 1 Overview",
              "content": [
                {
                  "type": "paragraph",
                  "text": "The first sophomore semester comprises of 4 CDCs, Mathematics III and Environmental Studies. All the CDCs as expected are an introduction to core chemical engineering with understandings of basic physics, chemistry and mathematics principles. Some of the courses are purely numerical and logic solving based while the others are theoretical and require reading and understanding of the content. Some courses also serve as pre-requisites for future courses. Though no previous knowledge about any such course is required, having a good grip of high school concepts like thermodynamics, fluids and differential equations helps the cause."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Chemical Process Calculations",
              "content": [
                {
                  "type": "paragraph",
                  "text": "Chemical Process Calculations is a very fundamental and hugely numerical course which serves as a basic introduction to the field of chemical engineering. It aims at inculcating systematic problem solving skills in students. It teaches one to solve various material balance problems with or without chemical reactions for single and multiple reaction groups. It includes further topics like bypass, recycle and purging during chemical reactions. It involves the use of thermodynamic tables, psychometric charts and basic thermodynamic principles. Furthermore, solving of material and energy balance problems simultaneously is done too. To ace this course, attending tutorial classes is a must. The problems and solutions discussed in tutorials are of extreme help throughout the course. Also, the professor expects a certain format of answering the problems which is also well taught in the tutorials. Lectures for this course are not a must but recommended. It is advised that you watch all lecture recordings and slides if available and understand the way of teaching of the professor. The book to this course is also very helpful. Before examinations and tests, glancing over and understanding the solved problems is quite helpful. If time permits, it is also recommended to solve and practice the end of chapter exercises, not all the questions but 2-3 of each type. Grading in this course is a bit harsh as in the solutions, either complete marks are given or zero. Its rare to get partial marks in a question if you have solved it partially correct. But scoring up till midsems is quite easy while compared to that, post midsems the course becomes tougher. So, try to maximize your scores in midsems and tutorial tests and not rely on compres to salvage your scores and grades. As such this course isn’t a pre-requisite to any future course but serves as a good base for fundamentals of chemical engineering. The material balance and energy balance methods are further required in other courses."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Fluid Mechanics",
              "content": [
                {
                  "type": "paragraph",
                  "text": "This is one of the most interesting courses in the semester. It is an introduction to the field of fluid mechanics. It mainly covers the basic principles of fluid dynamics and introduces one to fundamentals of basic fluid flow operations. The course deals with the basic principles of fluid flow analysis and behavior. It requires the recognition of basic meaning of pressure, density, viscosity, velocity fields etc. It also involves the applications of concepts like Reynold number, mass conservation, unsteady and steady state flows of fluids, buoyancy, shear stresses, viscous forces, laminar and turbulent flow, boundary layer concept, drag and lift. It then uses these concepts to explain fluid flow and behavior in chemical industry equipment and vessels. The course is taken by Mr. Pratik N. Sheth. The classes are quite interesting and engaging and it is advised to attend the lectures as well as tutorials to understand the course content thoroughly as the course comprises of mostly numerical and graphical solving. Practice previous year papers, solved examples and back exercises for preparation for midsems and compres. Sometimes same questions from old papers are given in the exam with just a little tweak or value changes. Slides and books are more than enough to understand and revise the contents. Tutorial tests are small and to the point of topics in syllabus and scoring good in them is easy. Also read and learn initial theories of each chapter because they are asked in the closed book section of exams. Grading for this course is generally good and fair to the students. You need to be average+ 50 to be on the safer side to receive an A grade which is quite achievable if you understand the numerical concepts and graphs. This course is pre-requisite for an elective Computational Fluid Dynamics which is an advanced and more diverse version of this course."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Chemical Engineering Thermodynamics",
              "content": [
                {
                  "type": "paragraph",
                  "text": "An extension of principles of thermodynamics in the field of chemical engineering. It’s a review of work, heat, reversible and irreversible processes. It also includes learnings of laws of thermodynamics to closed and open systems, heat effects, correlation for PVT behavior, maxwell relations and fluid properties. It involves the use of numerous equations for different conditions, which need not be memorized but just understood that when which equation is used. The course is taken by Mr. Ajay Pani. It’s a necessity to attend classes as well as tutorials as the whole course goes in continuation and has references from older topics throughout. So, a thorough understanding of the same is quite essential. For practice and examinations, the same methods and practices like Fluid Mechanics can be followed suit. Grading for this course too follows a similar behavior like Fluid Mechanics."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Engineering Chemistry",
              "content": [
                {
                  "type": "paragraph",
                  "text": "A purely theoretical course which involves the learnings of organic chemistry and reactions, physical chemistry including the thermos-physical and thermodynamic properties determination, adsorption equilibria, electrochemistry, analysis methods, water and waste water chemistry, corrosion, engineering materials, metals and alloys, polymers and fuel and its analysis. All lectures for this course is a must as whatever is taught in class, the examinations are framed based on that and that only. Sometimes those pieces of information are not available in the textbook. Notes for the same are recommended for quick revision and collection of all taught topics. The grading is a bit difficult as it is a low scoring course and averages vary quite a lot so the trend of grading varies too."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Mathematics III",
              "content": [
                {
                  "type": "paragraph",
                  "text": "You know the drill for the universal math course by this point. Religiously follow at least one source (any lecture section, Suresh Kumar, textbook, whichever floats your boat). I personally attended Jitender Sir’s classes and solved his problem sheets which I felt were sufficient. You can solve additional problems from the textbook until you gain confidence and practice PYQs before exams. For evaluations, give the quizzes a couple of days of prep as they have(had?) a pretty high weightage and be complacent with the buffer at the beginning because, at least for us, the content involved in the final quiz was the most challenging."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Semester 2 Overview",
              "content": [
                {
                  "type": "paragraph",
                  "text": "We have 4 CDCs this semester and POE/POM this semester. The CDCs take a step up and this is a tougher or maybe a more challenging semester than 2-1 as all the courses consist a great deal of numericals and also substantial theoretical information. So, buckle up for this semester as it is not going to be a tougher ride than 2-1."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Heat Transfer",
              "content": [
                {
                  "type": "paragraph",
                  "text": "Again, a very numerical based and contains tons of formulas. Involves learning of steady and unsteady state conduction, Fourier’s law, resistance in heat transfer, heat transfer in cartesian, cylindrical and spherical coordinates, insulations, convective heat transfer, analogy between momentum and heat transfer, condensation, radiation, heat exchangers, LMTD, NTU method, co current and counter current problems. Lectures for this course are recommended but not a daily must. Though be wary of the surprise lecture test factor which usually happens at the end of each chapter post midsems. Tutorials are recommended as the problems discussed in tutorials are sometimes as it is asked in tests. Slides are beneficial for exam preparations and it is recommended to get the book for the open book part and highlight and mark all the formulas in the book for easy reference during the exam. Previous year papers practice is a must as the pattern of questions is somewhat the same every year with few tweaks and changes. The grading for this course is like any other chemical numerical course and would seem mostly fair to everyone. Though there’s usually a very fine margin between A and A- so be careful:)."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Numerical Methods for Chemical Engineers",
              "content": [
                {
                  "type": "paragraph",
                  "text": "A very tedious and mind occupying course in general. It includes introduction to mathematical modelling and problem solving, use of MATLAB for equation and problem solving, error propagation, linear programming, linear and polynomial regression, Lagrange, inverse and spline interpolation and Fourier approximation, numerical differentiation and integration, differential equations and its engineering applications. As I liked to call it, this course is basically mathematics IV :). Lectures for this course are a choice, if you have a good mathematical base, you can basically do the whole course through slides and practice from text book. The whole course is purely and totally numerical. MATLAB will be taught in class but not in that depth and just for the ease of calculation. It won’t be considered as an evaluative component as the course doesn’t have any lab components. For exam preparations, thoroughly go through slides, practice the solved examples in class and tutorials, practice the assignment sheets and solve PYQs. The scoring and grading pattern for the course is same as Heat Transfer totally."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Material Science and Engineering",
              "content": [
                {
                  "type": "paragraph",
                  "text": "Both a theoretical and numerical course. This is one of the most complex courses in the semester in terms of understanding and application. It includes introduction to materials for engineering, metal structures, ceramics and polymers, crystalline structures, correlation of structure to properties and engineering functions, phase diagrams, heat treatment, polymers and composites, corrosion, evolution of materials and criteria for material selection. The professor for the course is a strict one and likes work to be done meticulously and properly, lacking which you can face serious consequences and mark deductions. Be thorough with your work and style in this course and be on time with everything and be honest most of all. The classes and tutorials are hugely beneficial, especially the tutorials as the examples discussed are very good and helpful for tests. Also don’t miss tutorials as attendance is recorded for them and often lecture content is carried on in tutorials too. For exam preparations, practice PYQs and back exercises. Solve tutorial examples and questions and also practice back exercises of the text book. Grading in this course is very general and as expected from a theoretical+numerical course. Because this course has a lot of evaluative components in terms of assignments so try scoring maximum in those so that you don’t lag behind as tutorial tests are quite tough and you might not be able to solve them once or twice."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Separation Processes I",
              "content": [
                {
                  "type": "paragraph",
                  "text": "A very fundamental and easy to understand course. It includes molecular diffusion in fluids, mass transfer, absorption, distillation, extraction, leaching etc. There are various types and methods of the said topics which are explained in great detail. The lectures for the course are very tedious as the professor takes a lot of extra classes and the syllabus runs slow up till midsems but after that the speed is picked up in such a way that if you don’t stay updated with what’s going on in class, you will surely lag behind. Tutorial problems are very basic but not in accordance with what is asked in tutorial tests or exams. For exams and test, practice PYQs and practice solved exampled in the text book and the back exercises of each type of question too. Grading is very fair for this course and usually in accordance with how you have performed throughout the sem. It is a high scoring course so you need to do good in all evaluatives to ace this course."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Principles of Economics",
              "content": [
                {
                  "type": "paragraph",
                  "text": "A very interesting and scoring course. Though it is a common course for everyone, you still have a good scope of scoring good in this course as the content is quite easy and in general it is a new course for everyone so there’s no partiality factor. Up until the midsems you don’t need to attend classes as much and everything can be done from slides, books and PYQs. But after midsems the content gets a bit complex so going to classes and tutorials is recommended. The scoring and grading are just like any other common course and is mostly fair to everyone for every grade."
                }
              ]
            },
            {
              "type": "subsection",
              "heading": "Humanities Electives",
              "content": [
                {
                  "type": "paragraph",
                  "text": "Print, Audio & Visual Advertisements (PAVA)\nThis in my opinion is the most interesting electives out of all. Taken by Sangeeta Sharma Ma’am, the course is super interesting and fun to participate in. Most of the evaluative weightage is to assignments in which you have to create a TV ad, a print ad and a website for your TV ad’s product. The whole process is fun and engaging, even the classes"
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "references": [],
  "appendix": []
}
]

# First_Year = [
#     {
#         {
#   "metadata": {
#     "title": "A WORD FROM THE CT'S",
#     "authors": [
#       "Anuj Wagh"
#     ],
#     "date": "",
#     "keywords": [
#       "Compre",
#       "exam tips",
#       "study guide"
#     ],
#     "source": "Final tips for Compre by CT's.pdf"
#   },
#   "sections": [
#     {
#       "heading": "YUVRAJ SHARMA",
#       "subsections": [
#         {
#           "heading": "MEOW 210/300",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "I would like to give you few tips which will help you land an A grade in MEOW."
#             },
#             {
#               "type": "numbered_list",
#               "items": [
#                 "Mid-Semester: To excel in mid-semester exams, solving Previous Year Questions (PYQs) is very important. Often, questions from PYQs resurface in exams. Additionally, aim for high scores in closed-book exams, as open-book exams can be notably more challenging.",
#                 "Comprehensive exam: The problems in Open Book exam will be of a much better level than those given in text book, so I recommend solving as many PYQ's as you can. In comprehensive exam there is a closed book section as well and it is pretty easy to score.",
#                 "Watch lectures if possible. Lectures not only elucidate theoretical concepts but also delve into the proofs of various theorems, making the subject matter more interesting.",
#                 "Tapomoy Guha sarkar sir is a really good teacher in oscillations and wave I really enjoyed learning from him. His teaching style was pretty amazing and I really do recommend him for the oscillations part. ALL THE VERY BEST!!"
#               ]
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "heading": "JAIRAM AYYAR",
#       "subsections": [
#         {
#           "heading": "GENCHEM 247.5/300",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "While the textbooks for this course have good questions, it is more important to solve the questions given in the tutorial classes and go through the PYQs."
#             },
#             {
#               "type": "paragraph",
#               "text": "PYQs are probably the most important resource for this course. Do solve the tut sheets. The questions in them have a really good level and important for testing your understanding of the concepts. PYQs are often repeated."
#             },
#             {
#               "type": "paragraph",
#               "text": "Quantum chemistry is almost completely new for most people and is difficult to understand in one go. Solving questions (PYQs) for this topic is very important as that is the only way you can learn how to apply the concepts taught in class."
#             },
#             {
#               "type": "paragraph",
#               "text": "Moreover, it is important to understand the spectroscopy part really well as numericals here, are scoring. Do try to solve questions, as a lot of different questions can be made from a single topic."
#             },
#             {
#               "type": "paragraph",
#               "text": "The textbook is important for Organic. DO NOT neglect the last part with the reactions/ stereochem as it may seem familiar from the entrance exam prep, but requires a very solid understanding of topics."
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "heading": "PRAJEET PARGANIHA",
#       "subsections": [
#         {
#           "heading": "GENBIO CT - 1.5",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "Tips for Excelling in a General Biology Comprehensive Examination:"
#             },
#             {
#               "type": "numbered_list",
#               "items": [
#                 "Class Notes: Your class notes will prove to be beneficial. If you missed any classes, consider borrowing notes from a friend who excels at note-taking. The material covered in lectures and tutorials is VERY important. Often, information not included in the slides is discussed during these sessions, and this information can be crucial for the open-book exam. Class notes also facilitate quick revision before the exam.",
#                 "Concepts: It's essential to have a crystal-clear understanding of the concepts. Many students fall into the trap of rote memorization without comprehending the material. Utilize any resources available to you, such as textbooks, reference books, NCERT, or the internet, to clarify any doubts.",
#                 "Textbook: If time permits, I personally recommend going through a reference book, as the main textbook lacks detail. The reference book can also be extremely useful during the open-book exam."
#               ]
#             },
#             {
#               "type": "annotation",
#               "text": "*THE CT STUDIED PCB IN HIS +2 (IS IN BPHARMA NOW) AND ALREADY HAS BIO KNOWLEDGE, SO HIS METHODS OF STUDYING MIGHT BE DIFFERENT. I HAVE HENCE TRIED TO GET ADVICE FROM MY WINGIE PRAJEET, A NON-MEDICAL BIO TOPPER."
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "heading": "AASHRAY JHADE",
#       "subsections": [
#         {
#           "heading": "EG 196/200",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "Engineering graphics is a very easy subject but most people neglect it unnecessary and lose grade. I just followed basics and solved all question PDFs provided by prof for practise and crossed checked the answers in questions with answers PDFs. I almost never did extra practice as such outside lab sessions. I did attend EG lectures which helped my imagination skills but I don't think they are necessary if you are good at imagination."
#             },
#             {
#               "type": "paragraph",
#               "text": "I always say, \"if you want A grade in EG, you don't need lectures. But if you want to understand what's actually happening, lectures are good\". I did teach and help my friends before exams, which was indirectly revision for me."
#             },
#             {
#               "type": "paragraph",
#               "text": "Some people go through lecture slides and watch videos related to it etc, I don't think it's necessary at all. Just practice questions again and again with proper understanding. You're good to go. Don't leave anything for later, understand everything that is being taught in lab sessions it self and chill. You won't even have to study for compres."
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "heading": "JAYANT KAPOOR",
#       "subsections": [
#         {
#           "heading": "ES 276/300",
#           "content": [
#             {
#               "type": "numbered_list",
#               "items": [
#                 "In ES, it doesn't matter if the exams are open book or closed book as there are not many lengthy equations to learn. The difficulty of questions in open book is always more than closed book and the time given is less, so prioritize solving all the questions that you know rather than finding similar examples in the book.",
#                 "Compres are pretty much similar to midsems and practicing questions is a must, you won't get a lot of time to prepare the last topic (transformers), so try to complete it from YouTube/online lectures beforehand. Sharda Ma'am's lectures (available on drive) are also very useful.",
#                 "I had Prof. Hari Om Bansal (IC) and Prof. Rajneesh Kumar as my lecturers and Prof. Karunesh Gupta as my tut instructor, all these teachers are highly skilled in teaching and I recommend referring their material."
#               ]
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "heading": "SNEH DESAI",
#       "subsections": [
#         {
#           "heading": "TRW 170/200",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "I would like to provide you with some tips to help you perform your best in the upcoming comprehensive examination."
#             },
#             {
#               "type": "numbered_list",
#               "items": [
#                 "Focus on Letter and Memo reports. They are post midsem topics and will have high weightage in compres. Observe sample reports and focus on the structures.",
#                 "All important parts of a report that were NOT asked in the assignment will be surely asked in the compres, so prepare accordingly. All the samples are available in the textbook.",
#                 "You must have a basic understanding of the pre midsem theory part. Use slides to revise.",
#                 "PRACTICE BY WRITING: This is a writing based course and just reading will not be enough. Therefore, practice writing different subparts a day prior to the exam. You can try practicing PYQs."
#               ]
#             }
#           ]
#         },
#         {
#           "heading": "WORKSHOP 260/300",
#           "content": [
#             {
#               "type": "paragraph",
#               "text": "Greetings, I am Sneh Desai, course topper of the Mechanical Workshop course. Some tips I would like to share for the upcoming compre examination are-"
#             },
#             {
#               "type": "numbered_list",
#               "items": [
#                 "Check PYQs before starting to know what type of questions are asked.",
#                 "The order for the best materials to study for the exam are CLASS NOTES >> SLIDES > TEXTBOOK.",
#                 "Try avoiding the previous year materials as topics taught change each sem.",
#                 "Practice subjective writing for the exam by attempting PYQs.",
#                 "Remember to learn formulas as the numericals are easy and scoring."
#               ]
#             }
#           ]
#         }
#       ]
#     }
#   ],
#   "references": [],
#   "appendix": [
#     {
#       "type": "paragraph",
#       "text": "To get a gist of the marks required for a good grade, please refer to the GRADES and AVERAGES in my Acads drive. I have added the previous year grades and cutoffs in this folder."
#      }
#      ]
#      }
#     }
# ]
# First_Year_Books = [
#     {
#         {
#         "metadata": {
#             "title": "BOOKS (First Year)",
#             "authors": [
#             "Abhishek Khurana (2021A7PS2688P)"
#             ],
#             "date": "",
#             "keywords": [
#             "first year",
#             "books",
#             "textbooks",
#             "reference books"
#             ],
#             "source": ""
#         },
#         "sections": [
#             {
#             "heading": "Thermodynamics",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Claus Borgnakke, Richard E. Sonntag, Borgnakke's Fundamentals of Thermodynamics, SI Version, Wiley India ed, ISBN: 9788126598199"
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Çengel Y.A. and Boles M.A., \"Thermodynamics: an engineering approach\", Tata Mcgraw-Hill, 2010, 6th ed.",
#                         "Booklet on Thermodynamic Tables, Figures & Charts Notes EDD-2007"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Technical Report Writing (TRW)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Mohan, R. C. & Krishna, S. (2016). Business correspondence and report writing: A practical approach to business & technical communication (Fifth). New Delhi: McGraw Hill Education (India) Private Limited."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Armer, T. (2011). Cambridge English for scientists (J. Day (ed.)). Cambridge: Cambridge University Press.",
#                         "Hewings, M. (2012). Cambridge academic English: An integrated skills course for EAP (Upper Intermediate) (South Asia). Cambridge: Cambridge University Press.",
#                         "Levrai, P., & Bolster, A. (2015). Academic presenting and presentations (Student's Book). A Linguabooks Publication.",
#                         "Raman, M., & Sharma, S. (2015). Technical communication: Principles and practice (Third). New Delhi: Oxford University Press.",
#                         "Sharma, R. C., Mohan, K., & Nirban, V. S. (2020). Business correspondence and report writing: A practical approach to business and technical communication (Sixth). New Delhi: McGraw Hill Education (India) Private Limited."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "GENERAL BIOLOGY",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Simon, E.J. et. al. Campbell Essential Biology with Physiology (5th edition). Noida: Pearson India Education Services Pvt. Ltd., 2016."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Enger, E.D., Ross, F.C. and David B. Bailey. Concepts in Biology (14th edition, BITS- Pilani Custom Edition 2012). New Delhi: Tata McGraw-Hill Publishing Company Ltd., 2012.",
#                         "Raven, P.H., et. al. Biology (9th edition). Singapore: McGraw-Hill Publishing Company Ltd., 2012.",
#                         "Starr, Cecie. Biology: Concepts and Applications (6th edition). India: Thomson Brooks/Cole, 2007"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "BIOLOGY LABORATORY",
#             "subsections": [
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Simon, E.J. et al: Campbell Essential Biology with Physiology (5th Edition, BITS Pilani custom edition). Noida: Perason India Education Services Pvt. Ltd., 2015"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Workshop Practice",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "B S Nagendra Parashar and R K Mittal, Elements of Manufacturing Processes, Prentice Hall of India, 2006, 4th print.",
#                         "Sangwan, K. S. et. al, Workshop Practice Manual, BITS Pilani."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Serope Kalpakjian and Steven R. Schmid, \"Manufacturing Engineering and Technology,\" Pearson Education, 4th edition, 2005, New Delhi"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Mathematics I (M1)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "J. Hass, C. Heil and M. D. Weir: Thomas' Calculus, 14th Edition, Pearson Education, 2018."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "E. Kreyszig: Advanced Engineering Mathematics, 10th Edition John Wiley and Sons 2011.",
#                         "T. M. Apostol: Calculus Vols I and II, 2nd Edition, John Wiley and Sons, 1967 and 1969."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Chemistry Laboratory",
#             "subsections": [
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Vogel's textbook of quantitative chemical analysis, Prentice Hall, 2000."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Computer Programming (CP)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Hanly, J.R. and E.B. Koffman. Problem Solving and Program Design in C (7/e). Pearson Education, 2013."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Patt, Yale. Introduction to Computing Systems: From bits & gates to C &beyond (2/e). McGraw Hill Education, 2017. (The authors take a bottom-up approach to introduce computers and computing).",
#                         "Forouzan, B.A. and Richard F. Gilberg. Computer science A structured programming approach using C (3/e). Cengage Learning, 2007. (The book gives a fairly comprehensive overview of C, with several example programs).",
#                         "Gottfried, B.S. and Jitender Chhabra. Programming with C (Schaum's Outlines Series, 3/e). McGraw Hill Education, 2017. (Another beginner's book on C programming, with lots of drill exercises and programs).",
#                         "Kernighan, B.W and Dennis Ritchie. The C Programming Language (2/e). Pearson Education India, 2015. (Considered the ultimate treatise on C, it conveys the philosophy and practice of C very tersely, but is pitched at an advanced beginner level).",
#                         "Das, S. Unix: Concepts and Applications (4/e). McGraw Hill Education, 2017. (Provides a great introduction to using Unix commands).",
#                         "Das, Sumitabha. Computer Fundamentals and C Programming. New Delhi, India: McGraw Hill Education. (2018)"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Mechanics Waves and Oscillations (MeOW)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "An Introduction to Mechanics by Kleppner & Kolenkow, Tata McGraw-Hill Indian Edition, 1999 (Please note: Given problem numbers will be followed from this edition only)",
#                         "Vibrations and waves, by A.P. French, CBS Publishers and Distributors, Inc., first Indian edition 1987."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Physics, Vol.1, by Halliday, Resnick, & Krane, 5th Edition, John Wiley & Sons, Inc., 2002",
#                         "The Physics of Waves and Oscillations by NK Bajaj, Tata McGraw-Hill 1984."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "General Chemistry",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "P.W. Atkins and Julio de Paula, Elements of Physical Chemistry: 6th Edition, Oxford University Press, Oxford, reprinted in 2015.",
#                         "T. W. Graham Solomons, Craig B. Fryhle, and Scott A. Snyder, Organic Chemistry, 12th Edition, John Wiley & Sons, Inc. New York, 2017"
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "J. D. Lee, Concise Inorganic Chemistry, 5th Edition, Blackwell Science, Oxford, 1999.",
#                         "David Ball, Physical Chemistry, Brooks/Cole Thomson Learning, 2003.",
#                         "J. E. Huheey, E. A. Keiter et al., Inorganic Chemistry: Principles of Structure and Reactivity, 4th Edition, Pearson Education, 1993.",
#                         "R. T. Morrison and R. Boyd, 'Organic Chemistry', 6th Edition, PHI, New Delhi, 1992."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Mathematics II (M2)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Elementary Linear Algebra with Supplemental Applications by H. Anton and Chris Rorres, 11th Edition, 2014, John Wiley & Sons.",
#                         "Complex Variables and Applications by R.V. Churchill and J.W. Brown, 8th Edition, 2014, McGraw-Hill."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Elementary Linear Algebra by S. Andrilli and D. Hecker, 4th Edition, 2012, Elsevier.",
#                         "Introductory Linear Algebra: An Applied First Course by Bernard Kolman and David R.Hill, 9th Edition, 2014, Prentice Hall.",
#                         "Introduction to Linear Algebra with applications by J. Defranza and D. Gagliardi, 2012, McGraw-Hill Education.",
#                         "A First Course in Complex Analysis with Applications by Dennis G. Zill & Patrick Shanahan, 2nd Edition, 2009, Jones & Bartlett.",
#                         "Complex Variables with Applications by A. D. Wunsch, 3rd Edition, 2004, Pearson Education"
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Engineering Graphics (EG)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "D.M. Kulkarni, A.P. Rastogi and A. K. Sarkar., Engineering Graphics with AutoCAD, PHI Learning Private Limited, New Delhi."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "N.D. Bhatt, Engineering Drawing, Charotar Publishing House, Gujarat."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Electrical Sciences (ES)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Leonard S. Bobrow and Navneet Gupta, Foundations of Electrical Engineering, Oxford University Press, Asian Edition, 2015."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Probability and Statistics (PnS)",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Devore, J. L., Probability & Statistics for Engineering and the Sciences, 8th Edition, Cengage Learning, 2012."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "REFERENCE BOOKS",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Milton, J. S. and Arnold J. C., Introduction to Probability and Statistics: Principles and Applications for Engineering and the Computing Sciences, 4th Edition, Tata McGraw-Hill, 2007.",
#                         "Walpole, R. E., Myers, R. H., Myers, S. L., Ye, K. E., Probability & Statistics for Engineers and Scientists, 9th Edition, Pearson Education, 2016.",
#                         "Johnson, R. A., Miller Freund's Probability and Statistics for Engineers, 8th Edition, PHI, 2010.",
#                         "Meyer, P. L., Introductory Probability and Statistical Applications, 2nd Edition, Addison-Wesley, 1970.",
#                         "Ross, S. M., Introduction to Probability Models, 11th Edition, Academic Press, 2014."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Physics Lab",
#             "subsections": [
#                 {
#                 "heading": "TEXTBOOK",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Laboratory Manual prescribed by the college (available at S9)."
#                     ]
#                     }
#                 ]
#                 }
#             ]
#             }
#         ],
#         "references": [],
#         "appendix": []
#         }       
#     }
# ]
# First_Year_Guide = [


#         {
#         "metadata": {
#             "title": "Subject Wise Gyaan 2021",
#             "authors": [
#             "Abhishek Khurana (2021A7PS2688P)",
#             "Mohit Singh (2021B3A71158P)",
#             "Shashwat Pandey (2021B1A12297P)",
#             "Abhijeet Singh (2021B5A72573P)",
#             "Shikhar Suryavanshi (2021B1A71694P)",
#             "Abhinav Lamba (2021B4A70913P)",
#             "Aryan Gupta (2021ABPS1672P)",
#             "Lakshya Sharma (2021A50388P)",
#             "Nishit Soni (2021A7PS0672P)"
#             ],
#             "date": "2021",
#             "keywords": [
#             "BITS Pilani",
#             "First Year",
#             "Study Guide",
#             "Course Tips"
#             ],
#             "source": "Subject Wise Gyaan 2021.pdf"
#         },
#         "sections": [
#             {
#             "heading": "M1 (MATH F111)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "In order to excel in this course, you have to practice questions. Being a common math course, getting an A is a bit competitive. Practice most of the suggested problems of the book \"Thomas Calculus\" provided in this drive. Practice all the tutorial sheets, and make a habit of maintaining a formula sheet for the entire course. Trust me, it will help in open book exams."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Midsems is the best evaluative to get a big lead among your batchies. Averages are relatively low and the course is relatively easy. Practice is the key to success. Read all the theorems from the book and this might be enough."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "After midsems the course becomes a bit tricky. I would recommend you to attend classes in order to visualize the integration limits and the green's theorem. As stated above, practice all the tutorial sheets and try to focus a bit more on solved examples and try to fully understand all of them. Post midsem syllabus might seem difficult but believe me its not. Attend classes to understand. Once you realize how to visualize the limits in a 3D plane, then the course becomes damn easy."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Not maintaining a formula copy. Helps a lot in open book exams",
#                         "Read all the theorems stated in boxes in the book \"Thomas Calculus\", and preferably write all of them in the formula copy of yours. Makes revision very easy.",
#                         "Fearing Post-Midsem syllabus - It might be a bit overwhelming to see all the integral limit visualizations but its easy. Attend the classes and try out some problems, it will surely help you.",
#                         "Practice as much as you can. At Least complete all tutorial sheets and some of the suggested problems."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in M1",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhishek Khurana (2021A7PS2688P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Computer Programming (CS F111)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "On the outset I would make one thing clear that this course definitely requires a lot of practice if you are new to C(programming language that they are going to teach you). Starting from array, things would start getting harder to understand. Pay attention to those topics and do practice questions related to those topics and by practice i mean you should see problems and write code on your own not just read the solutions and understand."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Till array part everything is going to be just theoretical, which i would recommend you should memorize because they ask it in tests a lot. More specifically there are questions on:"
#                     },
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Internal representation of data, Number System. This just needs some memorization.",
#                         "Arrays: This topic is easy to understand but questions based on this topic can be sometimes a little bit tricky so do practice its questions.",
#                         "Scope and storage classes: questions on this topic are tricky too so carefully read what it is asking. Also I would recommend you to do some research on this topic other than the slides."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Things from here start getting confusing. The end topics that are asked in the comprehensive exam and programming test, File handling and Linked List(most confusing topic) if I specify, requires a whole lot of practice to just understand."
#                     },
#                     {
#                     "type": "bullet_list",
#                     "items": [
#                         "Pointers: The most confusing topic imo:(. Do write codes of this topic and also try new things of your own other than the texts. Pro Tip: If you have clarity about this topic then your life would be easy :)",
#                         "Structures: Just get clarity in this topic it would help in the linked list.",
#                         "Dynamic Memory Allocation (DMA): Again a confusing topic.Get your concepts clear.",
#                         "File Handling: Relatively easy to understand, just through the slides.",
#                         "Linked List: Uses concepts of pointer,dma and structures. Hard topic to understand. There is at least one long question on this topic. Tip: Just get your concepts clear about pointers,dma and structures."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Labs",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Labs are like free marks so just attend."
#                     },
#                     {
#                     "type": "bullet_list",
#                     "items": [
#                         "Pro tip#1: Solve the required lab sheet one night before the class.",
#                         "Pro tip#2: Solving lab sheets on your own can get you 4 times ahead of your peers in the course!!!"
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Not writing codes on your own.",
#                         "Not solving the lab sheet.",
#                         "Always read the solutions and start thinking they have understood the topic.",
#                         "Not Solving pyqs."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in CP",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Mohit Singh (2021B3A71158P)\n Shashwat Pandey (2021B1A12297P)\n Abhijeet Singh (2021B5A72573P)\n Shikhar Suryavanshi (2021B1A71694P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Thermodynamics (BITS F111)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Thermodynamics is a course in which it is important to understand the previous topics in order to move forward, i.e., you cannot leave a topic in between as it will surely make your life difficult in understanding the upcoming concepts. Practice is the key to getting an \"A\" grade in this course. Practice at least all the questions being discussed in the tutorial sections and doing the previous year is a must as 30-40% of the questions asked are repeated. Adding to this you can try out the suggested problems from the book or just read the answers to have a quick revision."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Having a good grasp of the first two chapters will help you a lot. The main concept for the whole course is built on the same. These two chapters might seem easy, but try to practice as many problems from these chapters as it will for sure make your life much easier post midsem.",
#                         "Try to have a good hold on reading thermodynamic tables and make it a habit to use the table while practicing. It might seem useless but the major time wasted during the examination is finding values in the table, which can be prevented by following the above strategy."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "There's no new strategy for the post-midsem part as the concepts remain the same and you are just introduced with some new terms and formulas. Just follow the same strategy and surely you will excel in this course :)"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Jotting down wrong values from the table. Use tables while practicing.",
#                         "Fearing from the subject. - Practice as much as you can, the fear will surely go away.",
#                         "Learn all the graphs thoroughly. Nahi samajh aaye toh ratt lena:), will surely help."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in Thermodynamics",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhishek Khurana (2021A7PS2688P)\n Mohit Singh (2021B3A71158P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Workshop Practice",
#             "subsections": [
#                 {
#                 "heading": "Lab test",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Do attend all practice sessions before the practical test and try to form a good relationship with all lab instructors as it might help you boost your score by a few marks in the practical test."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Compre (Theory)",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Make sure you study the textbook thoroughly before the exam. Also go through all the solved examples as questions would be similar. Attending all theory classes would be the best option but if you are short on time they can be skipped. Do take a look at the PYQ's."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Not attending all lab sessions is the biggest mistake students make in this course. Not only do you lose your lab marks but you end up doing bad on your practical test. Another mistake most people make is not studying the course for the whole semester and starting on the last day. Make sure to give a few days to complete the syllabus and practice."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in Workshop",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhinav Lamba (2021B4A70913P)\n Aryan Gupta (2021ABPS1672P)\n Abhijeet Singh (2021B5A72573P)\n Shikhar Suryavanshi (2021B1A71694P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Technical Report Writing (BITS F112)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Focus majorly on stylistic errors and types of reports. Do remember all the definitions. It is slightly rote learning based but it is really beneficial to remember the slides."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Report",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Most important part is going through multiple reports from previous batches. This should be the first thing you do even before choosing a topic. DO NOT push things for the end moment, work for at least half to one hour per day. Coordinate with your group well and don't rush in choosing a topic. Think through and choose a topic which you find interesting yourself and know a little about. Stick to the format given by the instructor (very important). Senior reports might just be of different formats so keep that in mind. Read the slide of a particular section before typing it out. Reading slides of questionnaire is a must. Make sure to use tools like grammarly or quillbot you get with your bits id to curb plagiarism and check for grammatical errors. Spend time on your report, as this would greatly help you in your compres as well."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "If you worked well on your report, compre should be a cakewalk. They essentially ask you to write an introduction/ data analysis/ conclusion etc with respect to a certain question. Make sure to read the slides carefully and go through seniors' question papers and answers."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "It is a relatively lite course, but do not end up procrastinating. Slides are your best friend. Sometimes things in the slides and book won't match, in those cases stick to the slides. You could read the book if you want to for reference. Go through the slides at least 3-4 times before midsems as there is a lot to remember."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Not using tools like grammarly or quillbot.",
#                         "Doing silly grammatical mistakes in midsems/compres. Practice writing an answer or two before compres. Most of us haven't touched English since class 10, but you have to brush up on that or you'll end up losing marks to silly mistakes.",
#                         "Taking the report lite. The report could be a game changer for you, do not take it lite."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in Technical Report Writing",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Aryan Gupta (2021ABPS1672P)\n Shikhar Suryavanshi (2021B1A71694P)\n Abhinav Lamba (2021B4A70913P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "General Biology (BIO F111)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Don't skip any topic and try to make a strong grasp on topics such as ETC, Kreb cycle, glycolysis, Calvin Cycle DNA translation and transcription, meiosis, mitosis and difference between CAM, C4,C3 pathway etc. Try to score good in the midsems as the Av are not that high and getting decent grades and getting ahead of class in the beginning itself can be really helpful later."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Genetics and Recombinant DNA technology should be done thoroughly as many tricky and conceptual questions are framed from them. For Physiology, make proper notes and keep on revising them. Major Focus should be on Post Midsem syllabus in compres but don't skip the previous portion revise it at least once"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "The best strategy in Gen Bio is being regular and up-to-date with class. Be attentive during class or when watching lecture recordings and make detailed class notes as they can be a game changer during the open book component. Do regular revision of notes and if there is any conceptual difficulty in the topic watch short YouTube videos for that topic. If you have time you may even read the book although it is not necessary if you are thorough in the class. This subject can be one of the easiest to score with least effort if you are consistent and don't leave things for later."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Many Students find Gen-Bio relatively boring and take it lite.",
#                         "Not making detailed notes is a common mistake most of the students commit. Many direct questions are asked from lectures.",
#                         "Try not to skip any topic as the weightage of topics is very ambiguous and questions can be asked from topics you least expected (Tutorial Topics, self study portions).",
#                         "If not clear with your concepts especially in topics like genetics, DNA transcription and translation Re-wach lecture video, just do away with your doubts as many tricky questions are frames from them. Don't miss any in-class or take home assignment its meaningless to loose marks their and fall behind the class.",
#                         "Not reading the questions carefully is a common mistake students commit in all subjects but this can be really troublesome in gen bio as questions can be very tricky, read the questions carefully remember no matter how confusing it may seem everything is taught in class.",
#                         "Not writing all important points in exams, you may loose marks if you miss a important point or term even if your answer is correct. Be patient with the subject, keep on revising your notes, and keep on grinding :)"
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" Grade in Gen Bio",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Shikhar Suryavanshi (2021B1A71694P)\n Lakshya Sharma (2021A50388P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Chem Lab (CHEM F110)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Before the compres, make sure to go through pyqs, as many questions do repeat themselves. Make sure to learn important reactions associated with the experiments, Go through the manual and solve the questions given there.lts all basic JEE topics mainly the physical chemistry, questions based on stoichiometry, mole concept,titration are asked frequently so brush up your concept watch few oneshot videos online if you need.. Be punctual and always submit your assignments on time. Just remember the formulas and their applications and you'll score decent in compres."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Taking lab assignment lite and not submitting on time. These assignments are like free marks and can help you fetch an \"A\" grade easily."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" Grade in Chem Lab",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhinav Lamba (2021B4A70913P)\n Abhijeet Singh (2021B5A72573P)\n Shikhar Suryavanshi (2021B1A71694P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Physics Lab (PHY F110)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Before the compres, make sure to go through pyqs, as many questions do repeat themselves. Make sure you remember all the formulas associated with experiments, and some important points that each experiment has. Go through the manual and solve the questions given there. Be punctual and always submit your assignments on time. Just remember the definitions,reactions and their applications and you’ll score decent in compres."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Taking lab assignment lite and not submitting on time. These assignments are like free marks and can help you fetch an \"A\" grade easily."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A” Grade in Chem Lab",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhijeet SIngh(2021B5A72573P)\n Abhinav Lamba (2021B4A70913P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Biology Lab (BIO F110)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Attend all the labs and before every eval and compre try to read all the material provided twice and understand the concepts. If you have Gen Bio in the same semester you will have a slight advantage. Lot of question are framed from Photosynthetic pathways, Blood Grouping, Osmosis, Scientific Process so pay special attention to them.The pattern of the paper can vary and the questions can be tricky sometimes with confusing options in mcq , read the question carefully and think twice before attempting with a proper strategy depending upon the paper pattern. Never take labs lite because they are of only 1 credit remember all 3 labs combined can compensate for a 3 credit course that too with little efforts."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Loosing attendance marks in labs can be disastrous as few marks change grade so attend all the lab. Not completing the entire syllabus is a big blunder don’t leave any topics if short on time quickly go through the slides just once."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "“A” Grade in Bio Lab",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhijeet SIngh(2021B5A72573P)\n Shikhar Suryavanshi (2021B1A71694P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "M2 (MATH F112)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Pre midsem part completely includes the linear algebra part and the best source for learning is Shekhawat Sir’s youtube lectures. Linear algebra starts with the basic RREF stuff n all but than takes a sharp conceptual turn where half of the students leave the subject but try to avoid this and watch lectures twice if u don’t get it first.Complete understanding of basis,span and other common terms are essential for question solving, this Linear algebra part is the biggest chunk of the course total as- 30(quiz)+105(midsem)+60(compre). Tip-if u are not getting then try to do RREF, Axioms, Eigenvalues, these topics will assure around 40 marks in midsem[average crossed:)]"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Focus more on complex. It is relatively easier than Linear Algebra. You can easily score really well in compres just by Complex, I have done that personally. Read all the slides and go through all the examples given in them. If you can, solve the recommended questions from the book. The last part is connected with M1, so go through M1 concepts if you feel you should."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Try to understand the Linear part as it is a new thing for u and will become a headache if tried to gr"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Probability and Statistics (MATH F111)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "It is a very scoring course. The whole course revolves around some formulas, theorems and a bit of their application. The main challenging part of this course is to identify which type of distribution to apply in a given question. Maintain a formula copy and become comfortable with the notations in the formulas. Practicing most of the questions in the tutorial sheet might be enough to get a good grade in this course. SuKu lectures are a great resource."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "The most important thing in the “Probability” part of the course (pre-midsem) is to learn all the formulas and understand where to apply which formula. There are a certain keyword present in the question which hints at the distribution the question expects us to assume. Identify those keywords while practicing. Refer to the slides provided in the drive, a great resource."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Attend classes as you might feel this part of the course a bit illogical. As soon as you realize it's the same as pre-midsem with some new topics, continue the general strategy towards the course. Practice all tutorial sheets and continue to maintain the formula copy. Do practice PYQ"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Getting overwhelmed with a lot of formulas. With time you will get comfortable with them, just don’t stop studying this course as soon as you see the number of formulas to learn. :)"
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": None,
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Abhinav Lamba(2021B4A70913P)\n Nishit Soni (2021A7PS0672P)\n Abhishek Khurana (2021A7PS2688P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Mechanics Oscillations and Waves (PHY F111)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Everything is related to your jee mechanics so it would be easy to understand the topics. Some important topics that are asked in exams:"
#                     },
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Polar coordinates at least 1 question is asked from this topic so be thorough about.",
#                         "Mostly, derivation questions are asked from the momentum chapter.",
#                         "mostly numericals are asked from rotational motion and work and energy theorem."
#                     ]
#                     },
#                     {
#                     "type": "paragraph",
#                     "text": "Tip#1: If you want good scores in exams, solve the suggested problems of the books ;)\n Pro tip: Till midsems refer only to kleppner kolenkow."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "This part will be new to everyone and for this part refer to the slides and at least understand all the solved problems given in the slides. Textbook is also good, you may refer to that for better understanding of the topics. This part is more scoring and if you can't understand what's going on in the question then just learn the steps."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "The best strategy would be to keep up with the class ,understand and solve questions from the book(kk and a.p french) of the topics and at least 1-2 weeks before evaluatives start revising the questions again. But if you can't keep up with the classes then just at"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Students generally skip meow to study later which can pile up and in the end they don't understand anything and lose their grade. So it would be better to start early than to regret later."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "\"A\" grade in M.E.O.W",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Mohit Singh(2021B3A71158P)"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "General Chemistry (CHEM F111)",
#             "subsections": [
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "This course is nothing like the chemistry you used to study in JEE. Although you do get edge in some concept like isomerism, organic chemistry, if your JEE chemistry was strong. The course curriculum is application based and you need proper understanding of the concept to score good. Attend Classes or use the recorded lectures to go through the topics once and use the slides to revise the topics. Gen Chem slides are going to be your best friend during the entire course as they are one of the best planned and structured slides you will get for any course. Use them extensively and revisit and revise them as many times as you can. Practise the solved questions given in the slides. Prepare short notes which cover the formulas and the important concept and applications in few pages for quick revision, it would also come in handy during open book components. Detailed notes are not required as everything is covered in the slides in depth although if you are in a habbit of making notes you wil only benefit from it. Practise PYQs and slides questions, this is must and very important for scoring good in Gen Chem. REMEMBER : SLIDES+PYQ = GOOD SCORE in Gen Ch"
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Post midsem is where you will need to brush up your concepts from Jee as you have advanced version of many topics. But remember the questions asked are not to test your rote learning rather to test your understanding of the concept. Practice questions from slides and PYQs and use short YT videos to brush up on previous concept or any topic you find diificult. Study the Reaction mechanism for organic rection thoroughly. Dont leave the Pre Midsem portion during compre as a good percentage of questions are asked from their also ."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "numbered_list",
#                     "items": [
#                         "Students who didn’t use to like Chemistry in Jee make up their mind and take chemistry lite. It's a myth that you need a strong JEE background to score good in chemistry.",
#                         "Taking Evals and Quizzes Lite. Scoring good in evals is important if you want A in Gen Chem.",
#                         "Wasting Time by reading from books or revising JEE Topics as whole beforehand. Slides are enough for gen chem and revise JEE topics using your notes or YT videos when you face difficulties along the way.",
#                         "Not Practising enough PYQs. Questions can be tricky and you need practise especially for topics such as Spectroscopy, Term Symbols, Organic Chemistry etc."
#                     ]
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "“A” Grade in Gen C",
#                 "content": []
#                 }
#             ]
#             },
#             {
#             "heading": "Electrical Science (EEE F111)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Make sure to do a good amount of practice in Thevnin Norton part .This won't just help for the initial quizzes and mid sem but also in the future chapters and compre . Books will be the saver for you at any stage . Try to understand all the examples and practice some selected problems."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Post midsems ES gets slightly difficult but it'll be easy once you try to understand the concept. Lectures by Sharda Tripathi/Abhijit Asati will prove to be a blessing for you . She makes sure to cover a wide variety of illustrations for clarity of the topic."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Just try to follow the book as much as you can . Practice problems and PYQs and if you feel it's getting hard just go for lectures of Sharda Tripathi . If you follow conceptually ES will be very easy .Make sure you don't leave any topic. Sanjay vidhyadharan (a BITS prof) has some solved questions on his yt channel on different topics which can help you get a decent amount of practice additionally."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Common mistakes",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Leaving the subject completely if you don't understand initially. That's something you should never do . ES is a subject which gives you lots of opportunities to bounce back . Be"
#                     }
#                 ]
#                 }
#             ]
#             },
#             {
#             "heading": "Engineering Graphics (BITS F110)",
#             "subsections": [
#                 {
#                 "heading": "Pre-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Orthographic Projections is a relatively easy and scoring topic, try to score full. Lines and planes are tricky to get your head around at first, but once you get the hang of it, it’s just a game of practice. It is extremely important to remember the steps involved in the process. Try out all cases of lines and planes (in all quadrants). Try to score as much as you can in evals. Scoring well in midsems would be a game of practice and understanding."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "Post-Midsem",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "Isometric is a tricky topic for some, if that is the case for you, then only practice will help you. Go through pyqs to get a taste of the questions possible in evals. Try to link iso with ortho, that is essentially the most important part. Solids are a scoring topic, just like planes, remember the steps. It’s important to practice in autocad, as you would use many features in solids."
#                     }
#                 ]
#                 },
#                 {
#                 "heading": "General Strategy",
#                 "content": [
#                     {
#                     "type": "paragraph",
#                     "text": "It is essential to be regular, do NOT get a backlog. Attend all the labs as you’d learn at least something. You can afford a backlog pre midsem, but not in solids. Practice all the problems given by the profs and TAs. Your priority order should be Labs>Practice problems shared by the profs. After com"
#                     }
#                 ]
#                 }
#             ]
#             }
#         ],
#         "references": [],
#         "appendix": [
#             {
#             "type": "paragraph",
#             "text": "If you still have any more doubts, feel free to contact: Branch Wise Contacts.pdf"
#             }
#         ]
#         }
# ]



@mcp.tool()
# async def get_animals_by_species(species: str) -> List[Dict[str, Any]]:
#     """
#     Retrieves all animals of a specific species from the zoo.
#     Can also be used to collect the base data for aggregate queries
#     of animals of a specific species - like counting the number of penguins
#     or finding the oldest lion.

#     Args:
#         species: The species of the animal (e.g., 'lion', 'penguin').

#     Returns:
#         A list of dictionaries, where each dictionary represents an animal
#         and contains details like name, age, enclosure, and trail.
#     """
#     logger.info(f">>> 🛠️ Tool: 'get_animals_by_species' called for '{species}'")
#     return [animal for animal in ZOO_ANIMALS if animal["species"].lower() == species.lower()]

@mcp.tool()
# async def get_animal_details(name: str) -> Dict[str, Any]:
#     """
#     Retrieves the details of a specific animal by its name.

#     Args:
#         name: The name of the animal.

#     Returns:
#         A dictionary with the animal's details (species, name, age, enclosure, trail)
#         or an empty dictionary if the animal is not found.
#     """
#     logger.info(f">>> 🛠️ Tool: 'get_animal_details' called for '{name}'")
#     for animal in ZOO_ANIMALS:
#         if animal["name"].lower() == name.lower():
#             return animal
#     return {}

@mcp.tool()
def get_subject_details(subject_heading: str, guide: list) -> dict:
    """
    Retrieves details about a specific subject from the Second_Year_Guide JSON.

    Args:
        subject_heading (str): The heading of the subject to search for (e.g., "CHE F212, Fluid Mechanics").
        guide (list): The Second_Year_Guide JSON data.

    Returns:
        dict: Details about the subject, including paragraphs and bullet points.
    """
    for section in guide:
        for subsection in section.get("sections", []):
            for subsubsection in subsection.get("content", []):
                if subsubsection.get("heading") == subject_heading:
                    return {
                        "heading": subsubsection.get("heading"),
                        "content": subsubsection.get("content"),
                    }
    return {"error": f"Subject with heading '{subject_heading}' not found."}

if __name__ == "__main__":
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
    asyncio.run(
        mcp.run_sse_async(
        )
    )

