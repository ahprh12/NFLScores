import json
from match_parsing import get_match_scores, get_week_scores


#prints the cores in a readable way for testing purposes
def print_scores(scores):
    for score in scores:
        if score['type'] == 'FG':
            print('{} by {} for {} Yards'.format(score['type'], score['player'], score['yards']))
        elif score['play_type'] == 'run':
            print('{} run by {} for {} Yards'.format(score['type'], score['player'], score['yards']))
        elif score['play_type'] == 'pass':
            print('{} pass from {} to {} for {} Yards'.format(score['type'], score['passer'], score['player'], score['yards']))
        elif score['type'] == 'PAT':
            print('{} good by {}'.format(score['type'], score['player']))
        elif score['type'] == 'SF':
            print('Safety by {}'.format(score['player']))
        else:
            print('{} by {} for {} Yards'.format(score['type'], score['player'], score['yards']))


def write_to_json(scores, filename):
    with open('../output/' + filename, 'w') as writeJSON:
        json.dump(scores, writeJSON, sort_keys=True, indent=4)


def write_to_csv(scores, filename):
    f = open('../output/' + filename, 'w')
    headers = "player, type, yards, play type, passer\n"
    f.write(headers)
    for score in scores:
        f.write(score["player"] + "," + score["type"] + "," + score["yards"] + "," + score["play_type"] + "," + score["passer"] + "\n")
    f.close()

#gets all the score data from the week
scores = get_week_scores(2017, 2)
#print found scores to console and write to .json and .csv file
get_week_scores(2017, 2)
write_to_json(scores, 'stats.json')
write_to_csv(scores, 'stats.csv')
