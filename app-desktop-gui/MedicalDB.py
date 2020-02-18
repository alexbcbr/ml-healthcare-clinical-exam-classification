""" 
This is a class which represents the dataset
@author: Alex Coqueiro
@date: Feb, 2 2020
"""

import numpy

patientData = numpy.empty(10254, dtype=object)

patientData[10253] = { "name":"Maria Fuente", 
					   "photo": "data/patient_10253.jpeg",
					   "exam_full": "data/patient_10253_m.png",
					   "exam_frame": "data/Patient_10253_x501_y401.png",
					   "insulin_glyburide": "Up/Steady",
					   "patient_data": "17349435,Caucasian,Male,72,Old,Emergency,Discharged/transferred to another type of inpatient care institution, Transfer from another health care facility,2,MC,Family/GeneralPractice,36,0,8,0,0,1,5,None,None,No,No,No,No,No,No,No,Steady,No,No,No,No,No,No,No,No,No,Steady,No,No,No,No,No",
					 }

patientData[8975] = { "name":"Sue Sanchez", 
					  "photo": "data/patient_8975.jpeg",
					  "exam_full": "data/patient_8975_m.png",
					  "exam_frame": "data/Patient_8975_x2851_y1201.png",
					  "insulin_glyburide": "No/Down",
					  "patient_data": "23464296,Caucasian,Male,72,Old,Not Available,Discharged/transferred to another short term hospital,(null),9,MC,Psychiatry,17,1,11,0,0,0,9,>200,None,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No,No",
					}
