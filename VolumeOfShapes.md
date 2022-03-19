[Return to Readme](README.md)

        print("What type of shape would you like to find the volume of?")
        print("Enter CONE for cone")
        print("Enter CUBE for cube")
        print("Enter CYLINDER for cylinder")
        print()
        
        def ConeMath():
            CoRad = float(input("Radius of cone?: "))
            CoHei = float(input("Height of cone?: "))
            ConeVolume = 3.1415 * CoRad * CoRad * (CoHei/3)
            return ConeVolume

        def CubeMath():
            CuLen = float(input("Length of cube?: "))
            CubeVolume = CuLen * CuLen * CuLen
            return CubeVolume
        
        def CylinderMath():
            CyRad = float(input("Radius of cylinder?: "))
            CyHei = float(input("Height of cylinder?: "))
            CylinderVolume = 3.1415 * CyRad * CyRad * CyHei
            return CylinderVolume
        
        Answer = input("Input here: ")
        
        if( Answer == 'CONE'):
            total = ConeMath()
            print("The volume of the cone is: " + str(total))
        
        elif( Answer == 'CUBE'):
            total = CubeMath()
            print("The volume of the cube is: " + str(total))
            
        elif( Answer == 'CYLINDER'):
            total = CylinderMath()
            print("The volume of the cube is: " + str(total))
        
        else: print ("Unacceptable answer, please make sure answer is in all caps")
