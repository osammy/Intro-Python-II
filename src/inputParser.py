def inputParser(enteredInput):
    strippedInput = enteredInput.strip(" ")
    lengthOfInput = len(strippedInput)

    verbs = ['n','s','e','w','q','inventory','i','get', 'take', 'drop']

    if lengthOfInput == 1:
        if strippedInput == 'i':
            return {
                'err': False,
                'actionType': 'inventory',
                'inputEntered': strippedInput
            }
        if strippedInput not in verbs[:-3]:
            return {
                'err':True,
                'msg': f'Invalid Entry, please select either of {verbs[:-3]}'
            }
        return {
            'err': False,
            'actionType': 'move',
            'inputEntered': strippedInput
        }

    if lengthOfInput > 1:
        if strippedInput == 'inventory':
            return {
                'err': False,
                'actionType': 'inventory',
                'inputEntered': strippedInput
            }
        actions = strippedInput.split(" ")
        if len(actions) == 1:
            return {
                'err':True,
                'msg': f'Movement takes single charater, it could be any of {verbs[:-3]} instead'
            }

        if len(actions) > 2:
            return {
                'err':True,
                'msg': f'Expected a max of two args but got {len(actions)} instead'
            }

        if actions[0] not in verbs[-3:]:
            return {
                'err':True,
                'msg': f'Invalid Entry, please select either of {verbs[-3:]}'
            }
        return {
            'err': False,
            'actionType': actions[0], # This generally represents action type get or take
            'inputEntered': strippedInput,
            'splittedInput': actions
        }



        





