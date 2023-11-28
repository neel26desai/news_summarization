import requests
import json

# URL of your Flask server's endpoint (replace with your actual URL)
url = "http://20.163.29.17:80/predict"

# The data you want to send for prediction
# Replace this with the actual data you want to send
data = {
    "data": '''DALLAS -- November is usually a proving ground month for the Dallas Cowboys. With Thanksgiving always on their docket, Dallas is tasked with playing two games in the span of four days, which always makes for an interesting week.

 As has become something of a separate tradition, with a second consecutive Thursday game, the Cowboys will finish off playing three games in 12 days this week. Of course, winning makes the schedule more palatable and the Cowboys came out of the holiday two-fer with two wins, dominating both matchups, on their way to a three-game winning streak.

 The Cowboys beat their Thanksgiving week opponents by a combined score of 78-20, demonstrating that they have learned how to handle the festivities under head coach Mike McCarthy. It's the second year in a row that Dallas has swept both games of the holiday week after McCarthy had gone 1-3 in his first two years.

 Naysayers will point at the records of the Carolina Panthers (1-10) and Washington Commanders (4-8) to downplay the blowout wins. However, the Cowboys can only beat who they're scheduled to play each week and they only have to look north to the Detroit Lions to see what overlooking an opponent gets you during the annual Turkey day outing.

 Here's what else we learned about the Cowboys during the holiday stretch:

 Prescott strengthens MVP campaign

 Since their bye week during Week 7 back in mid-October, the Cowboys' offense has leveled up to become one of the best in the league, and it's led by their quarterback. Dak Prescott continued to build upon his MVP resume by throwing for six touchdowns without an interception in two efficient games.

 Against the Commanders, Prescott threw for 331 yards and four scores in his best Thanksgiving game since entering the league. Prescott also had the highest graded QB game in the league this year against his NFC East rivals.

 No QB in the league is playing as well as Prescott, who might be playing the best football of his career. The often unfairly-maligned Dallas signal caller led the NFL in touchdown passes entering the weekend.

 Offensive line elevating their play

 Part of the reason that the offense and Prescott are thriving is because the offensive line has done their best work recently. Their rushing attacks had back-to-back 100-yard games and Prescott has 70 pass attempts without a sack in the last two games.

 With the time to throw, and without being pressured, Prescott picked apart the defenses of the Panthers and Commanders. McCarthy's offense is thriving because the offensive line is paving the way for the unit to produce efficiently.

 The line needed time to get healthy and to work into a rhythm. By having the same starting five in the lineup over the past four weeks, you can see the unit beginning to gel.

 What red zone woes?

 One of the biggest problems with the Cowboys early in the season was their inability to convert red zone trips into touchdowns. At one point they were 27th in the league in red zone efficiency.

 Over the last two weeks, the Cowboys have ramped up their success rate. Against the Panthers and Commanders, the offense went 5-for-7 on their red zone trips, boosting the conversion rate to over 54%.

 Now punching it in more often than not, Dallas' rate is good enough to be in the top half of the league, ranking 16th through 12 weeks, and their efficiency has been rising, converting on 11 of their last 14 red zone opportunities.

 The success inside the 20-yard line has translated into more points on the scoreboard and has forced teams to try and come from behind to beat Dallas. That's not something that teams have had much success with this season.

 Bland bolstering Defensive MVP chances

 What a week it was for DaRon Bland, who has one of the more improbable stories that we've seen during the 2023 campaign. The second-year cornerback not only currently leads the league in interceptions, he also entered the NFL history books twice in the span of four days.

 In Carolina, Bland picked off rookie quarterback Bryace Young's pass and returned it for a score, tying the league record in a season with four pick-sixes. It took all of three quarters for Bland to gain sole possession of the record.

 On Thanksgiving, Bland picked off Washington quarterback Sam Howell and returned the interception 63-yards for the record-setting touchdown. Both pick-sixes were great plays from the fifth-round pick. Bland's ability to trail a play, use his catchup speed and length to make each interception proves that he's one of the most dangerous CBs in the league.

 With two scores in less than five days, one of which came with the nation watching on a holiday, Bland has put his name near the top of the list for Defensive Player of the Year. That's what happens when you make history.

 Cowboys continuing to produce blow outs

 What the Cowboys have accomplished during their victories so far this season has rarely been done, no matter the opponents. In their eight wins, seven have come by more than 20 points.

 In their last two games, the Cowboys have a +58 margin of victory, that's an impressive number despite the combined five wins this season from the Panthers and Commanders.

 Wins on the road have been hard to come by for the Cowboys in 2023, and beating an NFC East rival often comes down to the wire. Dallas had no such issues in either case over the last two weeks.

 McCarthy's group isn't just beating teams, they are dominating them. In a league almost designed to prove the 'any given Sunday' axiom, where games often come down to the final play, the Cowboys have been lighting up the scoreboard and running teams off the field instead.

 There's no shame in doing exactly what you're supposed to do and then some. The Cowboys won't and shouldn't apologize for crushing the bad teams on their schedule, even if they still have something to prove against teams that they might meet in the playoffs.'''
}

# Convert the data to a JSON string
data_json = json.dumps(data)

# Set the content type to application/json
headers = {'Content-Type': 'application/json'}

# Send the POST request to the server
response = requests.post(url, data=data_json, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the server
    print("Response from server:", response.json())
else:
    print("Failed to get response. Status code:", response.status_code)
