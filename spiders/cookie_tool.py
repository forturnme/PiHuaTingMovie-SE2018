def stringToDict(cookie):
        # 将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        itemDict = {}
        items = cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


mycookie = "time=MTEzNTI2LjIxNjM0Mi4xMDI4MTYuMTA3MTAwLjExMTM4NC4yMDc3NzQuMTE5OTUyLjExMTM4NC4xMDQ5NTguMTEzNTI2LjExMTM4NC4xMTU2NjguMTAyODE2LjEwMjgxNi4xMDcxMDAuMTA0OTU4LjExNzgxMC4xMDcxMDAuMA%3D%3D; DIDA642a4585eb3d6e32fdaa37b44468fb6c=1br023pdg16kmosvelsfn6lmj0; remember=MTEzNTI2LjIxNjM0Mi4xMDI4MTYuMTA3MTAwLjExMTM4NC4yMDc3NzQuMTE5OTUyLjExMTM4NC4xMDI4MTYuMA%3D%3D"
trans = stringToDict(mycookie)
print(trans)