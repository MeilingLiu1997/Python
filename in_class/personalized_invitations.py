def nameList(list):
    i = 0
    while i < len(list):
        newName = list[i]
        print('Date: 09/27/2016\n\nDear:', newName, '\nI am having a Halloween party on October 31st at my place.'
        'My address is 2130 Fulton Street, San Francisco, CA 94117.\nPlease let me know if you can make it.\n \n'
        'Your Name\n=============================')
        i += 1

def main():
    l = ['Tom','Jerry','David','Susan','Kay']
    nameList(l)

main()
