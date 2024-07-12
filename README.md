# Autonomous-Driving-and-Data-Collection-System

Objective:
Our objective is to design and implement a robust data collection and training system for autonomous driving using Grand Theft Auto V (GTA5) as the simulation platform. The system aims to gather synchronized data on vehicle dynamics, environment, and driving scenarios while offering scalability, flexibility, and ease of experimentation. By leveraging the immersive and dynamic environment of GTA5, we aim to create a comprehensive dataset for training AI models capable of autonomous vehicle.

Outcome:
The developed system enables efficient data collection, balancing, and training for autonomous driving models. By harnessing the capabilities of GTA5 and integrating custom mods and NPCs, we achieve a diverse and high-quality dataset. The system's flexibility allows for rapid experimentation with different training configurations, leading to improved model performance. Ultimately, the outcome is the advancement of autonomous driving technology through the creation of robust AI models capable of safe and effective vehicle control in various real-world scenarios.

Technologies:

•	Grand Theft Auto V (GTA5): Provides an immersive open-world environment for data collection and simulation.
•	Custom NPCs and Mods: Used to drive vehicles and customize the environment within GTA5 for data generation.
•	Server-Client Architecture: Facilitates communication between Data Collectors, Trainer, and Player instances, ensuring seamless coordination and data flow.
•	Machine Learning Frameworks: Utilized for model training, inference, and performance evaluation.
•	Custom Scripts: Developed to manage data collection, training, and player interactions within the system.
 


•	Visualization Tools: Employed for real-time monitoring and analysis of model predictions and system performance.



System Overview: 


2.1 Data Collectors:

The data collection process begins with Data Collector nodes, each running GTA5 with custom NPCs and mods. These nodes gather data such as image frames, car dynamics (acceleration, braking, steering), speed, and purpose (driving instructions). Multiple Data Collector instances can run concurrently, allowing for scalable data collection.

2.2 Server:

The central component of our system, the Server, facilitates communication between Data Collectors, Trainers, and Players. It loads configurations, manages connections, and distributes collected data to the Trainer for model training. Offers flexibility to adjust system settings dynamically, enabling seamless experimentation with various training configurations.

2.3 Trainer:

The Trainer receives balanced data samples from the Server and manages the training process.
Samples are stored in buffers until a sufficient number is collected for training. It periodically saves trained models and distributes them to connected Player instances.

2.4 Player:

Player instances connect to the Server to receive updated model parameters. They run their copies of the trained model in inference mode, making real-time predictions for vehicle control. Custom GTA5 mods facilitate the translation of model predictions into controller inputs, adjusting car steering accordingly.

3. Data Collection Process:

Data Collectors utilize custom NPCs to drive vehicles in GTA5, generating diverse scenarios for data collection. Collected data includes synchronized image frames, car dynamics, speed, and driving instructions. The process ensures high-quality data by capturing frames at a rate of 30 frames per second and balancing collected samples for variety.


4. System Flexibility:

The system is designed to be flexible, allowing rapid configuration changes and experimentation.
Output types for training, such as regression, classification, or discrete delta, can be adjusted independently for each parameter. Loss, metrics, and balancing mechanisms automatically adapt to reflect these settings, enhancing system versatility.

5. Player Experience and Monitoring:

Players connect to observe model performance and growth.
They receive updated parameters from the Trainer during gameplay, reflecting the latest model improvements. The Player Console provides real-time feedback on raw predictions and translated controller values, enabling monitoring of model behavior.

6. Future Development:

The project is in constant development, with ongoing efforts to enhance system capabilities.
Future iterations may involve optimizations for efficiency and performance, as well as the incorporation of advanced machine-learning techniques.


