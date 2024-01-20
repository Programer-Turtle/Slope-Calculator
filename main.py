import platform
import os

def ClearScreen():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def CalculateSlope(Data):
    if not isinstance(Data, dict):
        raise Exception("Data is not a dict.")
    y1 = Data["Y1"]
    y2 = Data["Y2"]
    x1 = Data["X1"]
    x2 = Data["X2"]

    SlopeRise = y2 - y1
    SlopeRun = x2 - x1

    if SlopeRise < 0 and SlopeRun < 0:
        SlopeRise *= -1
        SlopeRun *= -1

    slopeInFloatOrIntForm = SlopeRise / SlopeRun
    SlopeInFractionForm = f" {SlopeRise}\n---\n {SlopeRun}"

    FinalData = {
        "NumForm": slopeInFloatOrIntForm, 
        "FracForm": SlopeInFractionForm
        }
    return FinalData

def main():
    y1 = float(input("Y1:\n"))
    x1 = float(input("X1:\n"))
    y2 = float(input("Y2:\n"))
    x2 = float(input("X2:\n"))
    data = CalculateSlope({"Y1": y1, "X1": x1, "Y2": y2, "X2": x2})
    print(f"Number:\n{data["NumForm"]}\nFraction:\n{data["FracForm"]}")
    

if __name__ == "__main__":
    main()
