def inputParser(enteredInput):
    strippedInput = enteredInput.strip(" ")
    lengthOfInput = len(strippedInput)

    verbs = ['n','s','e','w','get', 'take']

    if lengthOfInput == 1:
        if strippedInput not in verbs[:-2]:
            return {
                'err':True,
                'msg': f'Invalid Entry, please select either of {verbs[:-2]}'
            }
        return {
            'err': False,
            'actionType': 'move',
            'inputEntered': strippedInput
        }

    if lengthOfInput > 1:
        actions = strippedInput.split(" ")
        if len(actions) == 1:
            return {
                'err':True,
                'msg': f'Movement takes single charater, it could be any of {verbs[:-2]} instead'
            }

        if len(actions) > 2:
            return {
                'err':True,
                'msg': f'Expected a max of two args but got {len(actions)} instead'
            }

        if actions[0] not in verbs[-2:]:
            return {
                'err':True,
                'msg': f'Invalid Entry, please select either of {verbs[-2:]}'
            }
        return {
            'err': False,
            'actionType':'secondary', # This generally represents action type get ot take
            'inputEntered': strippedInput
        }



        





