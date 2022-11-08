# class Cars:
#
#     def engine(self, name, max_speed):   # the stuff in the () are attributes/parameters
#         print(name, max_speed)
#
#     def transmission(self):
#         print("Hemi 6.2L")
#
#
# obj = Cars()
# obj.engine("Hemi", 140)
# obj.engine("SRT", 160)
# obj.transmission()
class Cars:

    def engine(self, name, max_speed):
        print( name, max_speed)

    def transmission(self):
        print("Hemi 6.2L")


obj = Cars()
obj.engine("HEMI", 140)
obj.engine("SRT", 180)
obj.engine("Mazda", 120)
obj.transmission()