.. |github-icon| replace:: 🐙

.. figure:: img/GeoAI_Banner_t.png

**Hands-on Geographical Artificial Intelligence (GeoAI)** introduces you to the foundational approaches and methods of machine learning and artificial intelligence applied to spatial data. Featuring new material and a technical ecosystem for modern spatial data science, this course covers everything from basic ML to deep learning, foundation models, and AI ethics.

This is a new, jointly developed course held collaboratively by the **Department of Built Environment, Aalto University, Finland** and the **Institute of Geodesy (Working Group Geoinformation), TU Graz, Austria**. 

.. important::
    Notice that the **course runs from 16.3. - 19.5.2026 (8 sessions)**. 
    **Registration deadline:** 12th March 2026 via `this form <https://forms.gle/rgCkE3tTLuc2PW9p6>`__.
    Teaching sessions for **Aalto University students** are held in **Otakaari 4, Espoo, Finland**.
    Teaching sessions for **TU Graz students** are held at **Rechbauerstraße 12, 8010 Graz, Austria**.

    **Aalto students:** If you still need to build your Python and GIS foundations, consider taking the
    *Geo-Python* and *Automating GIS-processes* courses (5 ECTS each) before this course —
    see `geo-python.github.io <http://geo-python.github.io/>`__ and `autogis.github.io <https://autogis.github.io/>`__.

Learning objectives
-------------------

After completing this course, you should be able to:

- **Explain and apply** machine learning and deep learning algorithms to geospatial data analysis problems
- **Process and analyze** geospatial imagery using AI-based computer vision methods
- **Use and evaluate** Large Language Models (LLMs) and Foundation Models for geospatial tasks
- **Identify and address** geospatial bias, fairness, and representativeness issues in AI systems *(AI Ethics)*
- **Apply and critically assess** state-of-the-art GeoAI methods in real-world scenarios

Prerequisites (Noncompulsory)
-----------------------------

Before taking this course, you should have:

1. **Experience with Python programming for GIS**
2. **Fundamental knowledge of Spatial Data Science**

**Python & GIS basics refresher:** If you need to refresh your skills, we strongly recommend going through the open online book
`Introduction to Python for Geographic Data Analysis <https://pythongis.org/>`__ by Tenkanen, Heikinheimo & Whipp (2025).

Supporting material
-------------------

**Course Specific Reading:**
For the introductory sessions, the following existing materials are highly recommended:

- `Git Basics Tutorial <https://sustainability-gis.readthedocs.io/en/latest/tutorials/git-basics.html>`__
- `Introduction to GeoAI <https://introsda.readthedocs.io/en/latest/lessons/L10/intro-to-GeoAI.html>`__

.. admonition:: Help improving the materials

    **This is a new joint course.**

    As a fast-evolving domain, the content of the course is likely to change and improve. By being a fully open
    educational resource, **you can also help making the course better**.
    If you find any errors, typos, or other problems, please help by suggesting an edit on GitHub.
    You can do this easily by clicking ``suggest edit`` under the |github-icon| **GitHub** icon located at the top-right of each page.

Course format & Ecosystem
-------------------------

The majority of the work for the course exercises will be programming in the Python language.
The course consists of Lecture/Practical (VU) sessions in which concepts are introduced and then immediately applied to real-world geospatial datasets.

The main tools and services we will use on this course include:

- **GitHub Classroom:** Used for hosting online lecture and practical materials.
- **LUMI Supercomputer:** Students will have access to the Finnish LUMI supercomputer for training models and running inference.

**Assessment / Grading:**
The final grade is based on practical assignments:

- 2 Individual Assignments
- 1 Collaborative Group Project (executed in mixed teams of students from both TU Graz and Aalto University)

Grading is based on the total points earned across all assignments:

.. list-table::
    :widths: 1 2 2
    :header-rows: 1

    * - Grade
      - Points required
      - Description
    * - 5 (excellent)
      - ≥ 90 %
      - Outstanding performance
    * - 4
      - 80 – 89 %
      - Very good performance
    * - 3
      - 70 – 79 %
      - Good performance
    * - 2
      - 60 – 69 %
      - Satisfactory performance
    * - 1 (pass)
      - 50 – 59 %
      - Adequate performance
    * - 0 (fail)
      - < 50 %
      - Insufficient performance

.. admonition:: University Specifics & Credits

    **ECTS Credits:** 3
    
    **TU Graz Students:** Course Number ``GST.416UF`` (Selected Topics of Geospatial Technologies).
    
    **Aalto University Students:** Special course on Geoinformatics under the Master's Programme of Geoinformatics. Course code: ``GIS-E6020``.

Program
-------

The course includes 8 teaching sessions running between March 16th and May 19th, 2026. Topics for the first two weeks are listed below:

.. list-table::
    :widths: 1 2 6
    :header-rows: 1
    :stub-columns: 1
    :align: left

    * - Week
      - Date, Time & Room
      - Themes
    * - 1
      - | 16.03.2026
        | 09:15–12:00 EET (Finland) / 08:15–11:00 CET (Austria)
        | Room 201
      - - **L0: Course Overview:** Information about the course, teaching format, grading format, timeplan, assignments, and rules.
        - **L1: Introduction into GeoAI:** History of AI, classification of AI, spatial information in AI, spatially explicit AI.
        - **Concepts in AI:** Explainability, fairness, bias.
    * - 2
      - | 23.03.2026
        | 09:15–12:00 EET (Finland) / 08:15–11:00 CET (Austria)
        | Room 201
      - - **L2: Machine Learning Basics:** Different types of algorithms (supervised, unsupervised, regression, classification).
        - **ML Workflows:** Terminology, training procedure, evaluation of models.
        - **P1: Machine Learning Practical:** Training a simple ML model, showcasing spatially explicit modeling, and predicting.
        - **Interactive:** Team building exercise (Miro board).


Contents
--------

.. toctree::
    :maxdepth: 1
    :caption: Course information

    course-info/course-info
    .. course-info/learning-goals
    .. course-info/grading
    .. course-info/course-environment-components
    .. course-info/slack-usage
    .. course-info/License-terms
    .. course-info/attribution
    .. course-info/resources
    .. course-info/installing-miniconda

.. toctree::
    :maxdepth: 1
    :caption: Exercises

    .. exercises/exercise-1
    .. exercises/exercise-2
    .. exercises/exercise-3

.. toctree::
    :maxdepth: 1
    :caption: Tutorials

    .. tutorials/git-basics
    .. tutorials/intro-to-python-geostack.ipynb
    .. tutorials/spatial_network_analysis.ipynb

.. toctree::
    :maxdepth: 1
    :caption: Week 1

.. toctree::
    :maxdepth: 1
    :caption: Week 2

    lessons/L1/intro-to-GeoAI