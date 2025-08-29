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
  "subjects": [
    {
      "subject": "CHE F211, Chemical process calculations",
      "content": [
        "The course is based on the principles of mass balance.",
        "You should be clear on the law of conservation of mass.",
        "This course becomes boring as soon as it starts, but it can be tricky to apply the logic as they have been taught in the class during your exams.",
        "Attend classes and tutorials regularly, you'll have a lot of tut tests in this subject, 6-7 spread through the semester so try and keep up with the classes.",
        "Practice questions done during lectures and tutorials to solidify your concepts.",
        "Examples from textbook, lecture material are the ideal resources to study.",
        "Strict grading, try and score as many marks in the tut tests as the mid sems and compres are lengthy and tricky to solve.",
        "Take inputs from the lecturer on how to do the assignments to score extra marks."
      ]
    },
    {
      "subject": "CHE F212, Fluid Mechanics",
      "content": [
        "This course is the basic introduction to fluid mechanics, covering the fundamental and practical aspects of fluid flow.",
        "It is an important technical subject which will be taken up during interviews if you opt for Core Chemical Sls.",
        "Also, a prerequisite for Chemical Lab-l which will come up during your 3-1.",
        "The recommended textbook (Fox, R.W. and A.T. McDonalds, Introduction to Fluid Mechanics (8th Ed.), John Wiley & Sons Inc., 2011.) is great, has good explanations for concepts and examples accompanying this.",
        "Dr, Pratik N Sheth was my instructor and his classes can be a little slow at times but you are recommended to go to lectures because he gives out problems during lecture hours which helps you understand the concepts and also, ace the tutorial tests.",
        "Lectures and tutorial hours are a must attend. There are 7 surprise tut tests out of which 6 are counted.",
        "These are open/closed books which are announced during the tut hour.",
        "It is easier to score for the tut tests as the aggregated average is generally low and you can score well above the average at the end of the semester.",
        "Mid-sem and Compre have both open and closed book tests and for which I recommend to brush up the examples and basics, the questions for the closed book tests can be direct and concept based whereas, for the open book you have to be thorough with practice.",
        "Grading is good, in a class of 120 students about 14 students got A grade.",
        "Average + 6-8 helps you get a B-."
      ]
    },
    {
      "subject": "CHE F213, Chemical Engineering Thermodynamics",
      "content": [
        "This course involves the application of the first and second laws of thermodynamics, basics that you've learned in Thermodynamics in your first year.",
        "Applications of work, heat, reversible and irreversible processes. Equation of states, generalized correlation for the PVT behavior.",
        "A lot of new and important concepts like the Maxwell relations, fluid property estimations, Gibbs-Duhem equation and Vapor Liquid Equilibria are introduced.",
        "We had lectures as well as tutorial tests. The lectures are fast paced but don't rush through the syllabus.",
        "The advantages of attending lectures is that it helps you cover most of the syllabus for the tutorial tests as you'll only have to practice examples given in the textbook.",
        "Although most of the content taught in the lecture is straight out of the textbook, it takes time to understand the basic concepts which are important if you are looking for a Core job as this is one of the important subjects.",
        "The recommended textbook (J. M. Smith,, H C Van Ness, M. M. Abbott and M. T. Swihart (Adapted by: B I Bhatt), Introduction to Chemical Engineering Thermodynamics (8th ed.), Tata McGraw Hill, special Indian Edition 2020.)is pretty much all you need to study.",
        "I would suggest all the examples from each of the chapters to be solved as the tut test questions as well as the open book questions in mid sem and compre are pretty straight forward.",
        "Mark the textbook well otherwise you'll be lost during open book exams.",
        "Like in Fluid Mechanics, try attempting all the tut-tests as they push you well above average.",
        "Open book marking is purely final answer based, so make sure to complete the questions in mid-sem and compres. Keep in handy all the values of gas constant for the closed book tests.",
        "A.K. Pani is an amazing teacher and will value you if you are regular in his classes."
      ]
    },
    {
      "subject": "CHE F214, Engineering Chemistry",
      "content": [
        "The course is about understanding the various developments in the field of water treatment, polymers, instrumental method of analysis, etc. The objective of the course is to study these areas in detail, and understand the important working principles of equipment involved.",
        "To score good marks in all the evaluations please attend lectures.",
        "The professor takes attendance very seriously and is partial towards people who attend classes.",
        "A lot of important material is taught during tutorial hours, so make sure you attend those.",
        "There are no surprise tests, all the tests will be announced beforehand.",
        "The recommended book (Vairam SRamesh SEngineering Chemistry, Wiley India, 2011) is very extensive, and lectures only cover like 45% of the material which is expected of you during examinations.",
        "There is a lot of material to learn because the course is completely closed book.",
        "Be regular with the reading of the textbook to not pile up just before exams.",
        "PYQs are important as they give an idea about important topics which you should focus on, like wastewater treatment is one of the most important topics.",
        "Strict checking and grading. Each word in your answer sheet will be evaluated for its relevance.",
        "To the point answers are expected. We also had an assignment which was evaluated on the basis of our knowledge of the topic and research work."
      ]
    },
    {
      "subject": "MATH F211, Mathematics-III",
      "content": [
        "This course is the study of differential equations with the introduction to solving boundary value problems using various classical methods.",
        "You have to have thorough knowledge of differential equations taught in calculus of +2.",
        "Attending lectures of Prof. Krishnendra Shekhawat, as along with basic concepts he gives out a lot of problems to solve during lecture hours which will make it easier to understand.",
        "Solve suggested questions from the textbook and pyqs to help understand as well as learn the concepts.",
        "Make marked notes to make sure you don't waste your time skimming through the notes during open book exams.",
        "It is a very high scoring subject and you need to really practice to know the type of questions asked and manage time efficiently during exams.",
        "2 out of 3 tut tests are considered which again are very high scoring so try to remain above average at all times.",
        "A grade was given on Av+ 75."
      ]
    },
    {
      "subject": "CHE F241, Heat Transfer",
      "content": [
        "The course is about the steady and unsteady state conduction, convection and radiation. It starts off with the basics of heat transfer due to conduction and convection that we’ve already learnt in class 12. Then the level increases with the introduction to fins and unsteady state convection. And then there will be many dimensionless numbers which will be in use like reynolds, grashoffs, nusselts, and it can be a little confusing at times.",
        "Lectures can keep you updated for the tut tests and you will understand how to solve the problems. The lectures are based on books and you will be solving a lot of questions to help with the concepts. There’ll be 6 tut-tests out of which 4 will be considered and 2 assignments before mid sem and compre respectively",
        "Understand the concepts using the recommended textbook (Holman, J.P., Bhattacharyya, S. (2011), “Heat Transfer”, 10th Ed., Tata McGraw Hill Education Pvt Ltd, New Delhi.), quick revision through slides, before mid sem and compre take the assignments seriously, similar questions are asked. Solve the given examples for practice and the questions covered during lecture hours. Give all the tutorial tests to stay well above average and take the pressure off mid sem and compre.",
        "Good grading depending on the class strength about 10 % people get A. This is an important subject if you want to study Transport Phenomenon and Computational Fluid Dynamics. The concepts will also be used in Chem Lab I in your 3-1.",
        "Don’t freak due to closed book tests as the questions asked are based on basic concepts taught in lectures. You don’t have to learn the bigger formulas, just the easy ones and know how to correlate the concepts."
      ]
    },
    {
      "subject": "CHE F242, Numerical Methods for Chemical Engineering",
      "content": [
        "This is the introduction to mathematical modeling and engineering problem solving. It will help students to use numerical techniques to solve allergic and differential equations. Learning numerical methods for differentiation, integration and curve fitting, which helps us solve various problems of Chemical engineering subjects.",
        "This course is all about problem solving and practice. Questions done during lecture hour, tutorial hour and PYQs. Try learning MATLAB along with this subject to get hold of the software as it is very important for chemical engineering.",
        "The textbook (Chapra, S. C. and R. P. Canale, Numerical Methods for Engineers, 7th Edition, McGraw Hill Education (India) Pvt. Ltd., New Delhi, 2015) has a lot of problems to practice, tutorial hours are important as there are many surprise tests.",
        "In a class of about 120 students 11-13 students get an A grade.",
        "There is a lot to remember for the closed book test so make sure you are in regular practice to not get confused between the concepts."
      ]
    },
    {
      "subject": "CHE F243, Material Science",
      "content": [
        "Introduction to various materials for engineering and their significant properties. You learn about metals, ceramics, polymers and composites. Corrosion of materials and the evolution of materials.",
        "The book is easy to understand but the questions asked are seldom from the book. Questions practiced during tutorial hours are important and direct questions are asked in the exams. Attending lectures is completely up to you.",
        "PYQs are important as the tests are mostly numerical with little to no theory asked.",
        "Strict grading for tests and assignments. You won’t be allowed in the class if you are 5+ mins late."
      ]
    },
    {
      "subject": "CHE F244, Separation Process I",
      "content": [
        "The most interesting subjects of 2-2. All you have to do is go to lectures, make notes and that’s it. It is about molecular diffusion in fluids, mass transfer, mass transfer coefficient and concepts involved in adsorption, stripping, distillation and liquid-liquid extraction. You’ll learn problem solving in the lectures and all the concepts are so well taught.",
        "To study this subject all you need are the notes and understanding the art of graphical problem solving which will be taught during lecture hours.",
        "Practice problems from assignments and PYQs, direct questions are asked in tut tests and mid sem compres.",
        "Important prerequisites for Chemical Lab I and Separation Process II. The grading is linenet."
      ]
    },
    {
      "subject": "ECON F211, Principles of Economics",
      "content": [
        "PoE is a foundation course that introduces us to the field of Economics and Finance. We are taught all the basics economics, micro and macro. It is an important course if you are thinking of pursuing a Finance Minor.",
        "PYQs is the best way to study the subject as the questions asked during tut tests and mid sem compres are very similar and you just need to know the methodology of solving certain problems.",
        "The recommended textbook is amazing, you get to learn everything through examples. If you find yourself not attending classes, I suggest you diligently read the textbook and keep up with the syllabus in order to not fall behind.",
        "About 700-800 students take up this course so it has a better range for grading but a lot of students tend to take lite and since it’s a very scoring subject averages are very high so don’t fall below the average line because it awards you a C grade."
      ]
    },
    {
      "subject": "Chemical Process Calculations",
      "content": [
        "Chemical Process Calculations is a very fundamental and hugely numerical course which serves as a basic introduction to the field of chemical engineering. It aims at inculcating systematic problem solving skills in students. It teaches one to solve various material balance problems with or without chemical reactions for single and multiple reaction groups. It includes further topics like bypass, recycle and purging during chemical reactions. It involves the use of thermodynamic tables, psychometric charts and basic thermodynamic principles. Furthermore, solving of material and energy balance problems simultaneously is done too. To ace this course, attending tutorial classes is a must. The problems and solutions discussed in tutorials are of extreme help throughout the course. Also, the professor expects a certain format of answering the problems which is also well taught in the tutorials. Lectures for this course are not a must but recommended. It is advised that you watch all lecture recordings and slides if available and understand the way of teaching of the professor. The book to this course is also very helpful. Before examinations and tests, glancing over and understanding the solved problems is quite helpful. If time permits, it is also recommended to solve and practice the end of chapter exercises, not all the questions but 2-3 of each type. Grading in this course is a bit harsh as in the solutions, either complete marks are given or zero. Its rare to get partial marks in a question if you have solved it partially correct. But scoring up till midsems is quite easy while compared to that, post midsems the course becomes tougher. So, try to maximize your scores in midsems and tutorial tests and not rely on compres to salvage your scores and grades. As such this course isn’t a pre-requisite to any future course but serves as a good base for fundamentals of chemical engineering. The material balance and energy balance methods are further required in other courses."
      ]
    },
    {
      "subject": "Fluid Mechanics",
      "content": [
        "This is one of the most interesting courses in the semester. It is an introduction to the field of fluid mechanics. It mainly covers the basic principles of fluid dynamics and introduces one to fundamentals of basic fluid flow operations. The course deals with the basic principles of fluid flow analysis and behavior. It requires the recognition of basic meaning of pressure, density, viscosity, velocity fields etc. It also involves the applications of concepts like Reynold number, mass conservation, unsteady and steady state flows of fluids, buoyancy, shear stresses, viscous forces, laminar and turbulent flow, boundary layer concept, drag and lift. It then uses these concepts to explain fluid flow and behavior in chemical industry equipment and vessels. The course is taken by Mr. Pratik N. Sheth. The classes are quite interesting and engaging and it is advised to attend the lectures as well as tutorials to understand the course content thoroughly as the course comprises of mostly numerical and graphical solving. Practice previous year papers, solved examples and back exercises for preparation for midsems and compres. Sometimes same questions from old papers are given in the exam with just a little tweak or value changes. Slides and books are more than enough to understand and revise the contents. Tutorial tests are small and to the point of topics in syllabus and scoring good in them is easy. Also read and learn initial theories of each chapter because they are asked in the closed book section of exams. Grading for this course is generally good and fair to the students. You need to be average+ 50 to be on the safer side to receive an A grade which is quite achievable if you understand the numerical concepts and graphs. This course is pre-requisite for an elective Computational Fluid Dynamics which is an advanced and more diverse version of this course."
      ]
    },
    {
      "subject": "Chemical Engineering Thermodynamics",
      "content": [
        "An extension of principles of thermodynamics in the field of chemical engineering. It’s a review of work, heat, reversible and irreversible processes. It also includes learnings of laws of thermodynamics to closed and open systems, heat effects, correlation for PVT behavior, maxwell relations and fluid properties. It involves the use of numerous equations for different conditions, which need not be memorized but just understood that when which equation is used. The course is taken by Mr. Ajay Pani. It’s a necessity to attend classes as well as tutorials as the whole course goes in continuation and has references from older topics throughout. So, a thorough understanding of the same is quite essential. For practice and examinations, the same methods and practices like Fluid Mechanics can be followed suit. Grading for this course too follows a similar behavior like Fluid Mechanics."
      ]
    },
    {
      "subject": "Engineering Chemistry",
      "content": [
        "A purely theoretical course which involves the learnings of organic chemistry and reactions, physical chemistry including the thermos-physical and thermodynamic properties determination, adsorption equilibria, electrochemistry, analysis methods, water and waste water chemistry, corrosion, engineering materials, metals and alloys, polymers and fuel and its analysis. All lectures for this course is a must as whatever is taught in class, the examinations are framed based on that and that only. Sometimes those pieces of information are not available in the textbook. Notes for the same are recommended for quick revision and collection of all taught topics. The grading is a bit difficult as it is a low scoring course and averages vary quite a lot so the trend of grading varies too."
      ]
    },
    {
      "subject": "Mathematics III",
      "content": [
        "You know the drill for the universal math course by this point. Religiously follow at least one source (any lecture section, Suresh Kumar, textbook, whichever floats your boat). I personally attended Jitender Sir’s classes and solved his problem sheets which I felt were sufficient. You can solve additional problems from the textbook until you gain confidence and practice PYQs before exams. For evaluations, give the quizzes a couple of days of prep as they have(had?) a pretty high weightage and be complacent with the buffer at the beginning because, at least for us, the content involved in the final quiz was the most challenging."
      ]
    },
    {
      "subject": "Heat Transfer",
      "content": [
        "Again, a very numerical based and contains tons of formulas. Involves learning of steady and unsteady state conduction, Fourier’s law, resistance in heat transfer, heat transfer in cartesian, cylindrical and spherical coordinates, insulations, convective heat transfer, analogy between momentum and heat transfer, condensation, radiation, heat exchangers, LMTD, NTU method, co current and counter current problems. Lectures for this course are recommended but not a daily must. Though be wary of the surprise lecture test factor which usually happens at the end of each chapter post midsems. Tutorials are recommended as the problems discussed in tutorials are sometimes as it is asked in tests. Slides are beneficial for exam preparations and it is recommended to get the book for the open book part and highlight and mark all the formulas in the book for easy reference during the exam. Previous year papers practice is a must as the pattern of questions is somewhat the same every year with few tweaks and changes. The grading for this course is like any other chemical numerical course and would seem mostly fair to everyone. Though there’s usually a very fine margin between A and A- so be careful:)."
      ]
    },
    {
      "subject": "Numerical Methods for Chemical Engineers",
      "content": [
        "A very tedious and mind occupying course in general. It includes introduction to mathematical modelling and problem solving, use of MATLAB for equation and problem solving, error propagation, linear programming, linear and polynomial regression, Lagrange, inverse and spline interpolation and Fourier approximation, numerical differentiation and integration, differential equations and its engineering applications. As I liked to call it, this course is basically mathematics IV :). Lectures for this course are a choice, if you have a good mathematical base, you can basically do the whole course through slides and practice from text book. The whole course is purely and totally numerical. MATLAB will be taught in class but not in that depth and just for the ease of calculation. It won’t be considered as an evaluative component as the course doesn’t have any lab components. For exam preparations, thoroughly go through slides, practice the solved examples in class and tutorials, practice the assignment sheets and solve PYQs. The scoring and grading pattern for the course is same as Heat Transfer totally."
      ]
    },
    {
      "subject": "Material Science and Engineering",
      "content": [
        "Both a theoretical and numerical course. This is one of the most complex courses in the semester in terms of understanding and application. It includes introduction to materials for engineering, metal structures, ceramics and polymers, crystalline structures, correlation of structure to properties and engineering functions, phase diagrams, heat treatment, polymers and composites, corrosion, evolution of materials and criteria for material selection. The professor for the course is a strict one and likes work to be done meticulously and properly, lacking which you can face serious consequences and mark deductions. Be thorough with your work and style in this course and be on time with everything and be honest most of all. The classes and tutorials are hugely beneficial, especially the tutorials as the examples discussed are very good and helpful for tests. Also don’t miss tutorials as attendance is recorded for them and often lecture content is carried on in tutorials too. For exam preparations, practice PYQs and back exercises. Solve tutorial examples and questions and also practice back exercises of the text book. Grading in this course is very general and as expected from a theoretical+numerical course. Because this course has a lot of evaluative components in terms of assignments so try scoring maximum in those so that you don’t lag behind as tutorial tests are quite tough and you might not be able to solve them once or twice."
      ]
    },
    {
      "subject": "Separation Processes I",
      "content": [
        "A very fundamental and easy to understand course. It includes molecular diffusion in fluids, mass transfer, absorption, distillation, extraction, leaching etc. There are various types and methods of the said topics which are explained in great detail. The lectures for the course are very tedious as the professor takes a lot of extra classes and the syllabus runs slow up till midsems but after that the speed is picked up in such a way that if you don’t stay updated with what’s going on in class, you will surely lag behind. Tutorial problems are very basic but not in accordance with what is asked in tutorial tests or exams. For exams and test, practice PYQs and practice solved exampled in the text book and the back exercises of each type of question too. Grading is very fair for this course and usually in accordance with how you have performed throughout the sem. It is a high scoring course so you need to do good in all evaluatives to ace this course."
      ]
    },
    {
      "subject": "Principles of Economics",
      "content": [
        "A very interesting and scoring course. Though it is a common course for everyone, you still have a good scope of scoring good in this course as the content is quite easy and in general it is a new course for everyone so there’s no partiality factor. Up until the midsems you don’t need to attend classes as much and everything can be done from slides, books and PYQs. But after midsems the content gets a bit complex so going to classes and tutorials is recommended. The scoring and grading are just like any other common course and is mostly fair to everyone for every grade."
      ]
    }
  ]
}
]

 



@mcp.tool()
async def get_subject_details(subject_heading: str) -> Dict[str, Any]:
    """
    Retrieves details about a specific subject from the Second_Year_Guide JSON.

    Args:
        subject_heading: The heading of the subject to search for (e.g., "Mathematics III").

    Returns:
        A dictionary containing the subject's heading and content, or an error message if not found.
    """
    logger.info(f"🛠️ Tool: 'get_subject_details' called for '{subject_heading}'")
    for section in Second_Year_Guide:
        for subject in section.get("subjects", []):
            if subject.get("subject") == subject_heading:
                return {
                    "heading": subject.get("subject"),
                    "content": subject.get("content"),
                }
    return {"error": f"Subject with heading '{subject_heading}' not found."}


if __name__ == "__main__":
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
    asyncio.run(
        mcp.run_sse_async(
        )
    )

