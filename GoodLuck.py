import random
welcome = '🃏\t🃏\t🃏\t🃏\t🃏'
credit = 17000
machine = random.randint(70,117 )

print('\t\t\t\t\t  Machine(',machine,')')
print("-GoodLuck-\t\t\t  💰Credit = ",credit)
print("Royal Flush\t\t\t\t\t\t\t\t 250,000\nStraight Flush \t\t\t\t\t\t\t  60,000\nFour-of-a-Kind \t\t\t\t\t\t\t40,000\nFull House \t\t\t\t\t\t\t\t\t  5,000\nFlush \t\t\t\t\t\t\t\t\t\t\t  3,500\nStraight \t\t\t\t\t\t\t\t\t\t  2,500\nThree-of-a-Kind\t\t\t\t\t\t\t  1,500\nTow Pair \t\t\t\t\t\t\t\t\t\t 1000")
print('\n\t\t\t',welcome)


while True:
    if credit >=400000:
        print(' \n                        ❌❌❌')
        print('              The machine is stoped')
        break
    color = ['❤️','♠️','♦️','♣️']
    card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    c1 = random.choice(card)
    c2 = random.choice(card)
    c3 = random.choice(card)
    c4 = random.choice(card)
    c5 = random.choice(card)
    co1 = random.choice(color)
    co2 = random.choice(color)
    co3 = random.choice(color)
    co4 = random.choice(color)
    co5 = random.choice(color)
    start = input('Open Round')
    if start == '' and credit > 0:
        credit -= 500
        print('--------------------------------------------')
        print('\t\t\t\t\t  Machine(',machine,')')
        print("-GoodLuck-\t\t\t  💰Credit = ",credit)
        print("Royal Flush\t\t\t\t\t\t\t\t 250,000\nStraight Flush \t\t\t\t\t\t\t  60,000\nFour-of-a-Kind \t\t\t\t\t\t\t40,000\nFull House \t\t\t\t\t\t\t\t\t  5,000\nFlush \t\t\t\t\t\t\t\t\t\t\t  3,500\nStraight \t\t\t\t\t\t\t\t\t\t  2,500\nThree-of-a-Kind\t\t\t\t\t\t\t  1,500\nTow Pair \t\t\t\t\t\t\t\t\t\t 1000")
        role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
        colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
        print('\n\t\t\t ',role)
        print('\n\t\t\t',colr)
        slct=''
        hold=''
        if c1==c2:
            hold=c1+c2
            slct='12'
        elif c1==c3:
            hold=c1+c3
            slct='13'
        elif c1==c4:
            hold=c1+c4
            slct='14'
        elif c1==c5:
            hold=c1+c5
            slct='15'
        elif c2==c3:
            hold=c2+c3
            slct='23'
        elif c2==c4:
            hold=c2+c4
            slct='24'
        elif c2==c5:
            hold=c2+c5
            slct='25'
        elif c3==c4:
            hold=c3+c4
            slct='34'
        elif c3==c5:
            hold=c3+c5
            slct='35'
        elif c4==c5:
            hold=c4+c5
            slct='45'
        if c1==c2 and c3==c4:
            hold=c1+c2+c3+c4
            slct='1234'
        elif c1==c3 and c2==c4:
            hold=c1+c3+c2+c4
            slct='1234'
        elif c1==c4 and c2==c3:
            hold=c1+c4+c2+c3
            slct='1234'
        elif c1==c5 and c3==c4:
            hold=c1+c5+c3+c4
            slct='1345'
        elif c1==c5 and c2==c4:
            hold=c1+c5+c2+c4
            slct='1245'
        elif c2==c5 and c1==c3:
            hold=c2+c5+c1+c3
            slct='1235'
        elif c2==c5 and c3==c4:
            hold=c2+c5+c3+c4
            slct='2345'
        elif c3==c5 and c2==c4:
            hold=c3+c5+c2+c4
            slct='2345'
        elif c4==c5 and c1==c2:
            hold=c4+c5+c1+c2
            slct='1245'
        elif c4==c5 and c3==c2:
            hold=c4+c5+c3+c2
            slct='2345'
        elif c1==c5 and c2==c3:
            hold=c1+c5+c2+c3
            slct='1235'
        elif c2==c5 and c1==c4:
            hold=c2+c5+c1+c4
            slct='1245'
        elif c3==c5 and c1==c4:
            hold=c3+c5+c1+c4
            slct='1345'
        elif c3==c5 and c1==c2:
            hold=c3+c5+c1+c2
            slct='1235'
        elif c4==c5 and c1==c3:
            hold=c4+c5+c1+c3
            slct='1345'
        if c1==c2==c3:
            hold=c1+c2+c3
            slct='123'
        elif c1==c2==c4:
            hold=c1+c2+c4
            slct='124'
        elif c1==c3==c4:
            hold=c1+c3+c4
            slct='134'
        elif c1==c4==c5:
            hold=c1+c4+c5
            slct='145'
        elif c2==c3==c4:
            hold=c2+c3+c4
            slct='234'
        elif c2==c3==c5:
            hold=c2+c3+c5
            slct='235'
        elif c2==c4==c5:
            hold=c2+c4+c5
            slct='245'
        elif c3==c4==c5:
            hold=c3+c4+c5
            slct='345'
        elif c1==c3==c5:
            hold=c1+c3+c5
            slct='135'
        elif c1==c2==c5:
            hold=c1+c2+c5
            slct='125'
        if co1==co2==co3==co4:
            hold=co1+co2+co3+co4
            slct='1234'
        elif co2==co3==co4==co5:
            hold=co2+co3+co4+co5
            slct='2345'
        elif co1==co2==co4==co5:
            hold=co1+co2+co4+co5
            slct='1245'
        elif co1==co2==co3==co5:
            hold=co1+co2+co3+co5
            slct='1235'
        elif co1==co3==co4==co5:
            hold=co1+co3+co4+co5
            slct='1345'
        if co1==co2==co3==co4==co5:
            hold=co1+co2+co3+co4+co5
            slct='12345'
        if c1==c2==c3==c4:
            hold=c1+c2+c3+c4
            slct='1234'
        elif c2==c3==c4==c5:
            hold=c2+c3+c4+c5
            slct='2345'
        elif c1==c2==c4==c5:
            hold=c1+c2+c4+c5
            slct='1245'
        elif c1==c2==c3==c5:
            hold=c1+c2+c3+c5
            slct='1235'
        elif c1==c3==c4==c5:
            hold=c1+c3+c4+c5
            slct='1345'
        print('Auto Hold: ',hold)
        print('\t Cancel Hold(c)\t\tContinue(return)')
        auhd=input('C/Re: ')
        if auhd=='c':
            slct = input('Hold:    1️⃣\t 2️⃣\t 3️⃣\t4️⃣\t5️⃣\n')
        if slct =='':
            c1=random.choice(card)
            c2= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co1=random.choice(color)
            co2=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='1':
            c2= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='2':
            c1= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co1=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='3':
            c2= random.choice(card)
            c1=random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co1=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='4':
            c2= random.choice(card)
            c3=random.choice(card)
            c1=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co1=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='5':
            c2= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            c1=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            co1=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='12' or slct=='21':
            c3=random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co3=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='13' or slct=='31':
            c2= random.choice(card)
            c4=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='14' or slct=='41':
            c2= random.choice(card)
            c3=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='15' or slct=='51':
            c2= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='23' or slct=='32':
            c1= random.choice(card)
            c5=random.choice(card)
            c4=random.choice(card)
            co1=random.choice(color)
            co5=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='24' or slct=='42':
            c1= random.choice(card)
            c3=random.choice(card)
            c5=random.choice(card)
            co1=random.choice(color)
            co3=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='25' or slct=='52':
            c1= random.choice(card)
            c3=random.choice(card)
            c4=random.choice(card)
            co1=random.choice(color)
            co3=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='34' or slct=='43':
            c1= random.choice(card)
            c2=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co1=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='35' or slct=='53':
            c2= random.choice(card)
            c1=random.choice(card)
            c4=random.choice(card)
            co2=random.choice(color)
            co1=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='45' or slct=='54':
            c2= random.choice(card)
            c3=random.choice(card)
            c1=random.choice(card)
            co2=random.choice(color)
            co3=random.choice(color)
            co1=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='123' or slct=='321' or slct =='213' or slct=='231':
            c4=random.choice(card)
            c5=random.choice(card)
            co4=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='134'or slct=='143'or slct=='314'or slct=='341'or slct=='413'or slct=='431':
            c2=random.choice(card)
            c5=random.choice(card)
            co2=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='234'or slct=='243'or slct=='342' or slct =='324' or slct=='423' or slct=='432':
            c1=random.choice(card)
            c5=random.choice(card)
            co1=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='345'or slct=='354'or slct=='534'or slct=='543'or slct=='435'or slct=='453':
            c2= random.choice(card)
            c1=random.choice(card)
            co2=random.choice(color)
            co1=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='135'or slct=='153'or slct=='315'or slct=='351'or slct=='513' or slct=='531':
            c2= random.choice(card)
            c4=random.choice(card)
            co2=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='124'or slct=='142'or slct=='214'or slct=='241'or slct=='412'or slct=='421':
            c3=random.choice(card)
            c5=random.choice(card)
            co3=random.choice(color)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='125'or slct=='152'or slct=='215'or slct=='251'or slct=='512'or slct=='521':
            c3=random.choice(card)
            c4=random.choice(card)
            co3=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='245'or slct=='254'or slct=='425'or slct=='452'or slct=='542'or slct=='524':
            c3=random.choice(card)
            c1=random.choice(card)
            co3=random.choice(color)
            co1=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif slct =='235'or slct=='253'or slct=='325'or slct=='352'or slct=='523'or slct=='532':
            c1= random.choice(card)
            c4=random.choice(card)
            co1=random.choice(color)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif ('1'and'2'and'3'and'4')in slct and '5' not in slct:
            c5=random.choice(card)
            co5=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif ('5'and'2'and'3'and'4')in slct and '1' not in slct:
            c1=random.choice(card)
            co1=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif ('1'and'2'and'4'and'5')in slct and '3' not in slct:
            c3=random.choice(card)
            co3=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif ('1'and'3'and'4'and'5')in slct and '2' not in slct:
            c2=random.choice(card)
            co2=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif ('1'and'2'and'3'and'5')in slct and '4' not in slct:
            c4=random.choice(card)
            co4=random.choice(color)
            role = c1+'\t\t'+c2+'\t   '+c3+'\t   '+c4+'\t  '+c5
            colr = co1+'\t '+co2+'\t'+co3+'\t'+co4+'\t'+co5
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        elif '1'and'2'and'3'and'4'and'5' in slct:
            print('\n\t\t\t ',role)
            print('\n\t\t\t',colr)
        
        
        if '10'in role and'J'in role and'Q'in role and'K'in role and'A'in role  and (co1==co2==co3==co4==co5):
            print("\n\t\t\t\t\t\t   Royal Flush\n\t\t\t\t\t    win'250000'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 250000
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                        else:
                            break
                            
        elif (('A'in role and '2'in role and '3' in role and '4' in role and '5' in role )or('2'in role and '3'in role and '4' in role and '5' in role and '6' in role)or ( '3'in role and '4'in role and '5' in role and '6' in role and '7' in role)or ('4'in role and '5'in role and '6' in role and '7' in role and '8' in role)or ('5'in role and '6'in role and '7' in role and '8' in role and '9' in role)or ('6'in role and '7'in role and '8' in role and '9' in role and '10' in role)or('7'in role and '8'in role and '9' in role and '10' in role and 'J' in role)or('8'in role and '9'in role and '10' in role and 'J' in role and 'Q' in role)or('9'in role and '10'in role and 'J' in role and 'Q' in role and 'K' in role))and (co1==co2==co3==co4==co5):
            print("\n\t\t\t\t\t   Straight Flush\n\t\t\t\t\t    win'60000'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 60000
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        elif (c1==c2==c3==c4)or(c2==c3==c4==c5)or(c1==c2==c4==c5)or(c1==c2==c3==c5)or(c1==c3==c4==c5):
            print("\n\t\t\t\t\t   Four-of-a-Kind\n\t\t\t\t\t    win'40000'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 40000
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        elif ((c1==c2==c3)and(c4==c5))or((c1==c2==c4)and(c3==c5))or((c1==c3==c4)and(c2==c5))or((c1==c4==c5)and(c2==c3))or((c2==c3==c4)and(c1==c5))or((c2==c3==c5)and(c1==c4))or((c2==c4==c5)and(c1==c3))or((c3==c4==c5)and(c1==c2))or((c1==c3==c5)and(c2==c4))or((c1==c2==c5)and(c3==c4)):
            print("\n\t\t\t\t\t\tFull House\n\t\t\t\t\t    win'5000'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 5000
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        elif (co1==co2==co3==co4==co5):
            print("\n\t\t\t\t\t\t   Flush\n\t\t\t\t\t    win'3500'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 3500
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        
        elif ('A'in role and '2'in role and '3' in role and '4' in role and '5' in role )or('2'in role and '3'in role and '4' in role and '5' in role and '6' in role)or ( '3'in role and '4'in role and '5' in role and '6' in role and '7' in role)or ('4'in role and '5'in role and '6' in role and '7' in role and '8' in role)or ('5'in role and '6'in role and '7' in role and '8' in role and '9' in role)or ('6'in role and '7'in role and '8' in role and '9' in role and '10' in role)or('7'in role and '8'in role and '9' in role and '10' in role and 'J' in role)or('8'in role and '9'in role and '10' in role and 'J' in role and 'Q' in role)or('9'in role and '10'in role and 'J' in role and 'Q' in role and 'K' in role)or('A'in role and '10'in role and 'J' in role and 'Q' in role and 'K' in role):
            print("\n\t\t\t\t\t\t   Straight\n\t\t\t\t\t    win'2500'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 2500
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        elif (c1==c2==c3)or(c1==c2==c4)or(c1==c3==c4)or(c1==c4==c5)or(c2==c3==c4)or(c2==c3==c5)or(c2==c4==c5)or(c3==c4==c5)or(c1==c3==c5)or(c1==c2==c5):
            print("\n\t\t\t\t\tThree-of-a-Kind\n\t\t\t\t\t    win'1500'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 1500
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d >0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b'and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
        elif c1==c2 and c3==c4 or c1==c3 and c2==c4 or c1==c4 and c2==c3 or c1==c5 and c3==c4 or c1==c5 and c2==c4 or c1==c5 and c2==c3 or c2==c5 and c1==c3 or c2==c5 and c1==c4 or c2==c5 and c3==c4 or c3==c5 and c1==c4 or c3==c5 and c2==c4 or c3==c5 and c1==c2 or c4==c5 and c1==c2 or c4==c5 and c1==c3 or c4==c5 and c3==c2:
            print("\n\t\t\t\t\t\tTow Pair\n\t\t\t\t\t    win'1000'")
            print("\tSend to Credit(c)\t\t\t Double(d)")
            d = 1000
            while True:
                choose = input('choose: ')
                if choose=='c':
                    credit += d
                    print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
                    break
                elif choose == 'd' and d>0:
                    while True:
                        print('\t\t\t\t\t\t',d,'\n\t Big(b)          Smal(s)          Back(bk)')
                        dch = input('B/S: ')
                        if dch =='bk':
                            break
                        elif dch =='b' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[7:]:
                                if d >400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d = 0
                                print('\t\t\t\t\t\t Lost💸')
                                break

                        elif dch =='s' and d < 400000:
                            x = random.choice(card)
                            c = random.choice(color)
                            print('\t\t ',x,'\n\t\t',c)
                            if x == '7':
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
                            elif x in card[:7]:
                                if d > 400000:
                                    break
                                else:
                                    d = d * 2
                                    continue
                            else:
                                d=0
                                print('\t\t\t\t\t\t Lost💸')
                                break
    elif start == 'q':
        print("\n\t\t\t\t\t\tYOU WON\n\t\t\t\t\t\t",credit,"\n\t\t\t\t\t\t💰💰💰💰")
        break
    elif start=='' and credit <= 0:
        print("\t\t\tYour Credit is Empty")
        print("\t\tEnter the number of mony")
        rep=input()
        credit = int(rep)
        print("GoodLuck\t\t\t\t\t\t Credit = ",credit)
    
        
        