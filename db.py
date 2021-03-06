--Questions
INSERT INTO `questions` (`id`, `question_text`, `recommendation`) VALUES
('2', 'Does your facility provide adequate privacy in all areas where care is provided, or patient’s information is taken including initial screening point, consulting rooms, pharmacy, wards, etc?', 'Ensure to provide privacy for patients in all relevant areas. Provide screens and curtains where applicable, re-organize the various units to ensure privacy and ensure consulting and counselling rooms and doors are closed doors when in use.'),
('3', 'Do you have a written plan for patient education and records are kept of the education provided to patients?', 'Develop a schedule to guide patient education in the facility. This should include the dates for the training, specific topics to be treated and the individual taking the training. Keep records of the outcome of the training conducted.'),
('4', 'Do you have health education materials on display in formats understood by patients?', 'Display relevant education materials at relevant units to inform clients. Where necessary ensure these materials are in a language (most spoken local language) or format (pictures) that is understood by patients.'),
('5', 'Have you displayed the designation (Hospital, Clinic, Maternity Home, e.t.c), services provided and the opening hours on site and do these reflect what is done?', 'Design and display a signpost onsite which clearly states the designation of the facility as approved by the Health Facilities Regulatory Agency, the services provided and the opening hours of the facility.'),
('6', 'Have you labelled the various units in your facility and are there directional signs to guide people to the right places?', 'Label the various units and rooms in your facility and display directional signs to guide people to various areas.'),
('7', 'Do you have an effective system for managing health information such that all relevant data in the facility is timely captured, aggregated and regularly analyzed to give the desired information about your operations?', 'Establish an effective (electronic or manual) system to timely capture, aggregate and periodically analyze all relevant data (patients, service, financial, administrative etc.) to obtain meaningful information. Document guidelines to guide staff on how to manage information in your facility.'),
('8', 'Does your patients\' record storage (be it electronic or paper-based) offer adequate confidentiality and safety? Do you have defined levels of access for the various categories of staff?', 'Ensure that patients\' record storage offers adequate safety and security; this includes lockable well-organized storage space for paper records and secured access for electronic records. Ensure that individuals\'(staff) access to patient records are clearly defined and adhered to.'),
('9', 'Do you have written policies and procedures on infection prevention control program (IPC) which guide the staff in implementation?', 'Establish infection prevention and control program with guiding policies and procedures covering all activities relevant to IPC including hand washing; use of personal protective equipment (PPE); handling of patient care equipment and soiled linen; prevention of needle/sharp injuries; management of healthcare waste; sterilization processes; and effective ventilation precautions (to prevent airborne droplets).'),
('10', 'Do you have adequate hand washing facilities available in all relevant areas?', 'Provide hand washing facilities at the OPD areas, consulting rooms, laboratory, and Pharmacy, wards, nurses station all washrooms and ensure an adequate supply of single-use hand towels, soap and running water at all times.'),
('11', 'Do you have posters and guidelines to remind staffs and patients of effective hand washing?', 'Display hand washing guidelines at the hand washing units to facilitate effective hand washing. Also, display at vantage locations posters to remind both staffs and patients to wash their hands.'),
('12', 'Do you have adequate PPE (gloves, gowns, etc.) available for staff at all relevant areas and do they understand and use them correctly?', 'Provide adequate PPE (gloves, gowns, face masks, googles, safety boots etc.) for staffs at all relevant areas; keep adequate inventory on them to ensure constant sufficient availability. Develop guidelines for their use indicating when to use them and how to use them and monitor adherence.'),
('13', 'Do you have a guideline for post-exposure prophylaxis (PEP) which also indicates where and how staff can obtain PEP?', 'Develop a guideline for post-exposure prophylaxis indicating the steps to be followed in an exposure. Include in the guideline, relevant details of individuals to contact or report to, and documentation required in the process.'),
('14', 'Does your facility have clean, functional sanitary facilities (toilets, washrooms, sluice areas etc.) sufficient for both patients and staff?', 'Provide clean and functional toilets and washrooms for both staffs and patients. Establish a cleaning schedule for the cleaning of these areas and ensure cleaning activities are logged by both the cleaner and supervisor.'),
('15', 'Do you have adequate waste bins positioned at all relevant units and use colour-coded bag and bins for proper waste segregation?', 'Procure colour-coded bins and rubber liners/bag for all units in accordance with (inter)national colour coding system. Display guidelines to help in effective segregation of waste at waste generation point through to disposal.'),
('16', 'Do you have an SOP that guides staff in decontaminating, cleaning and sterilization procedures to prevent infections, including how to wrap packs for sterilization and checking sterility of autoclave and packs?', 'Document SOP to guide staff in decontaminating, cleaning and sterilization procedures, including how to wrap packs for sterilization and check sterility of autoclave and packs. Train staff in these and monitor adherence.'),
('17', 'Do you have an autoclave, and other materials for autoclaving (paper and sterility tapes etc.)?', 'Procure an autoclave, autoclaving paper and sterility tapes. Provide guidelines on sterilization and ensure to train staffs on sterilization, the use of autoclaving paper and sterility tapes.'),
('18', 'Do you have a clean, secure and organized storage unit(s) for pharmaceuticals and general products with its temperature monitored?', 'Ensure there is designated space for the storage of medications and medical &amp;amp;amp; general consumables. Provide shelves, lockers and racks where necessary and ensure items are neatly arranged &amp;amp;amp; labelled and space kept clean. Provide a room thermometer and ensure the temperature is monitored and logged daily.'),
('19', 'Do you have an inventory management system i.e. either electronic or paper-based (use of stock cards and registers) which helps in tracking stocks?', 'Establish a mechanism for documenting, monitoring and tracking the use of inventory in the facility. Provide tally cards and inventory registers to be used in inventory management. (Procure electronic inventory management where there is the capacity). Train staff on the inventory system adapted and ensure to document monthly analysis of inventory usage.'),
('20', 'Does your facility have access to ambulance or other officially designated means of transporting patients when an emergency referral is required?', 'Obtain contact details of the national ambulance service or contacts of other private ambulance facilities available in the area. Display these contacts at vantage locations of the facility for use when required. Where Taxis are used, display contacts of at least three reliable drivers with whom the facility has established contracts. Monitor performance on agreement e.g. response time, cleanliness of vehicle.'),
('21', 'Have you established contacts and arrangements with various health facilities/ service providers where you send clients who require all services your facility cannot provide to? Do you have a list of these facilities and their contact details displayed at relevant units?', 'Identify appropriate referral facilities for all relevant services which you would require to refer patients (maternal care, surgery, labs, diagnostics etc.) for services, create an up to date list of all referral facilities contact details. Display list at required units such as emergency unit, consulting rooms, lab etc.&quot;'),
('22', 'Do you maintain records of referrals? Do you fill and sign standardized referral forms with copies kept on patients file and keep referral register with outcomes of referral?', 'Design a standardized referral form for use in the referral of cases. All establish a system to keep records of all referrals made. This document should record details of patient referred, facility referred to, the outcome of referral and all information obtained from contacting the facility and patient.');

--Answers
INSERT INTO `answer_answer` (`question_id`, `answer`, `choice`, `needs_recommendation`) VALUES
('18', 'Not Applicable.', 'D', 0),
('10', 'Hand washing units are mostly not available or very insufficient.', 'C', 1),
('5', 'The designation and opening hours are clearly displayed and reflect the services the facility offer.', 'A', 0),
('15', 'There are adequate colour-coded bins and bags in all areas where necessary.', 'A', 0),
('20', 'Other arranged transportation, e.g. commercial vehicles (taxis) is used and this is reliable.', 'B', 1),
('9', 'I have no written IPC program in place and there are significant gaps in our IPC practices.', 'C', 1),
('19', 'There is no system in place.', 'C', 1),
('10', 'Hand washing units are available but either soap or hand towels are not adequate or some relevant units do not have the facilities.', 'B', 1),
('20', 'There is a well-equipped ambulance or active contacts list for other ambulance services.', 'A', 0),
('16', 'The SOPs available are not adequate but staff generally know what to do and mostly do them correctly.', 'B', 1),
('18', 'I have a clean store room which is secured, well organized and the temperature is monitored regularly.', 'A', 0),
('17', 'There is a functional autoclave and autoclaving paper and sterility tapes are available.', 'A', 0),
('11', 'Hand washing posters and guidelines are not available.', 'C', 1),
('22', 'There are standardized referral forms which are filled and signed, and an up to date referral register.', 'A', 0),
('2', 'Privacy is ensured in all areas.', 'A', 0),
('8', 'There is limited or no secured storage and no restriction of access to patients\' records.', 'C', 1),
('14', 'Sanitary facilities are sufficient, clean and in working order and cleaning schedules/logs are implemented.', 'A', 0),
('14', 'Sanitary facilities are sufficient and clean but there is no cleaning schedule or some of the facilities were not functioning well.', 'B', 1),
('8', 'Patients\' records storage is mostly safe, secured but levels of access have not been defined.', 'B', 1),
('22', 'Forms are filled and signed and kept on file but there is no referral register.', 'B', 1),
('22', 'There is no standardized referral form.', 'C', 1),
('21', 'There is no list of referral facilities.', 'C', 1),
('8', 'Patients\' records storage is safe, secure and accessible to only authorized personnel.', 'A', 0),
('07', 'I have an effective (electronic or manual) system in place and information is adequately managed.', 'A', 0),
('13', 'I have a protocol to be followed by staff in case of exposure but no guidelines on how to access PEP or persons to report to.', 'B', 1),
('2', 'Most areas offer adequate privacy (at least 3 of the above areas).', 'B', 1),
('11', 'Posters are displayed at relevant locations to remind staffs and patients and there are hand washing guidelines to aid appropriate handwashing at all units.', 'A', 0),
('5', 'Neither of them is displayed or they are largely not a reflection of the services offered.', 'C', 1),
('19', 'There is an inventory management system which is up to date.', 'A', 0),
('9', 'I do not have written IPC program; some documented procedures and IPC practices are in place but no monitoring system is in place.', 'B', 1),
('2', 'Privacy is not ensured in most areas.', 'C', 1),
('20', 'Not Applicable.', 'D', 0),
('18', 'There is a storeroom but not well organized, clean or temperature is not monitored.', 'B', 1),
('3', 'There is no patient education plan and a record is not kept of patient educations done.', 'C', 1),
('11', 'Either poster for reminders or hand washing guideline are available, or both are available but at limited locations.', 'B', 1),
('6', 'All units/departments in the facility are labelled and directional signs are provided.', 'A', 0),
('6', 'The units are not labelled or some of the labels are wrong.', 'C', 1),
('19', 'There is an inventory management system but records are not well kept.', 'B', 1),
('16', 'There is no SOPs and significant gaps exist.', 'C', 1),
('22', 'Not Applicable.', 'D', 0),
('20', 'There is no clearly defined process of transporting patients.', 'C', 1),
('17', 'There is a functional autoclave but either the equipment does not meet the facility\'s sterilization needs or autoclaving materials are not available.', 'B', 1),
('21', 'There is a list of referral facilities but there are no contacts and arrangement/ arrangement exist for few services.', 'B', 1),
('6', 'The units or departments are labelled but directions are not available or labelling and directional signs are in place but not adequately done.', 'B', 1),
('12', 'PPEs are available but there is no guideline for their use or staff use them incorrectly or staff do not use them most times.', 'B', 1),
('15', 'Waste bins are adequately available but not colour coded.', 'B', 1),
('13', 'There are no PEP guidelines.', 'C', 1),
('18', 'There is no dedicated storeroom or it is not secured.', 'C', 1),
('12', 'PPEs are not available or PPEs are not adequate', 'C', 1),
('3', 'I have a written plan or schedule for patient education and records of education provided are available.', 'A', 0),
('7', 'I have no effective system in place.', 'C', 1),
('1', 'I have patient rights charter on display at vantage points and implement policies that ensure patient and family rights are adequately recognized in our operations.', 'A', 0),
('1', 'I have no patient’s rights charter at all.', 'C', 1),
('4', 'Education materials which are easily readable are adequately displayed in a language/format understood by most clients.', 'A', 0),
('4', 'Education materials are not available or those displayed are insufficient.', 'C', 1),
('16', 'There are SOPs describing these procedures. Staff understand and follow them correctly and sterility checks are recorded.', 'A', 0),
('3', 'I have a written plan or schedule for patient education but no records of education provided or vice-versa', 'B', 1),
('10', 'Hand washing units are available with sufficient soap, hand towels and hand sanitizers.', 'A', 0),
('15', 'Waste bins are not adequate.', 'C', 1),
('4', 'Not Applicable.', 'D', 0),
('3', 'Not Applicable.', 'D', 0),
('21', 'My facility has an established arrangement/ contacts for referral of all services and I have an up to date list of referral facilities and their contact details.', 'A', 0),
('12', 'Sufficient PPEs are available. There are guidelines for their use and staff use them correctly all the time.', 'A', 0),
('14', 'Sanitary facilities are mostly not clean.', 'C', 1),
('4', 'Education materials are displayed but not clear and not understood by most clients.', 'B', 1),
('13', 'I have a protocol to be followed by staff in case of exposure and guidelines on how to access PEP as well as a list of persons to report to.', 'A', 0),
('17', 'Not Applicable.', 'D', 0),
('1', 'I have patient rights charter on display, at least at one point but I have no policy guiding how it is integrated into our operations.', 'B', 1),
('7', 'Not Applicable.', 'D', 0),
('21', 'Not Applicable.', 'D', 0),
('17', 'There is no functional autoclave.', 'C', 1),
('7', 'I have a system for collecting and aggregating data but not in a timely manner or the data collected is not analyzed into useful information.', 'B', 1),
('5', 'The designation is displayed but opening hours or the services provided are not displayed or vice versa.', 'B', 1),
('9', 'I have written infection prevention and control (IPC) program with policies and procedures, my staff is aware of the various infection control measures, and adherence is monitored and recorded.', 'A', 0);