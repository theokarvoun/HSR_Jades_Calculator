class Jade_Calc:
    def daily(days) -> int:
        return days*60
    def moc_stage(stage) -> int:
        if (stage <= 8):
            return stage*60
        return (6*60+(stage-6)*80)
    def moc_stars(stars) -> int:
        if (stars <= 24):
            return (int)(stars/3)*60
        return (int)(6*60+int((stars-18)/3)*80)
    def pf_stars(stars) -> int:
        if (stars <= 8):
            return stars*60
        return (8*60+(stars-8)*80)
    def as_stars(stars) -> int:
        if (stars <= 8):
            return stars*60
        return (8*60+(stars-8)*80)
    def weekly_su(weeks,eq_level):
        match eq_level:
            case 0:
                return weeks*75
            case 1:
                return weeks*75
            case 2:
                return weeks*105
            case 3:
                return weeks*135
            case 4:
                return weeks*165
            case 5:
                return weeks*195
            case 6:
                return weeks*225
    
if __name__ == "__main__":
    test = Jade_Calc
    print(f"Daily: {test.daily(days=3)}\nMOC(stage): {test.moc_stage(stage=7)}\nMOC(stars): {test.moc_stars(stars=21)}")