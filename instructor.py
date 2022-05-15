class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__avg_feedback=None
        self.__technology_skill=None
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    def set_experience(self,experience):
        self.__experience=experience
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill


    def get_instructor_name(self):
        return self.__instructor_name
    def get_experience(self):
        return self.__experience
    def get_avg_feedback(self):
        return self.__avg_feedback
    def get_technology_skill(self):
        return self.__technology_skill


    def check_eligibility(self):
        if self.__experience>3:
            if self.__avg_feedback>=4.5:
                return True
            else:
                return False
        else:
            if self.__avg_feedback>=4:
                return True
            else:
                return False
    def allocate_course(self,technology):
        for i in range(len(self.__technology_skill)):
            if technology==self.__technology_skill[i]:
                return True
        return False
instructor=Instructor()
instructor.set_instructor_name('Devi')
instructor.set_experience(4)
instructor.set_avg_feedback(4.5)
instructor.set_technology_skill(['python','C++','java'])
instructor.check_eligibility()
print(instructor.allocate_course('python') and instructor.check_eligibility())