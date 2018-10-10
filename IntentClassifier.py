from subprocess import call, check_output

#intents list
intent1 = ['mage ginume sheshaya keeyada','ginume sheshaya keeyada','sheshaya keeyada','mage ginume ithiriya keeyada','ginume ithiriya keeyada','ithiriya keeyada','mata mage ginume sheshaya danaganna puluwnda','mata mage ginume ithiriya danaganna puluwnda']
intent2 = ['mata salli thanpath karanna oni','salli thanpath karanna oni','mudal thanpath karanna oni','salli danna oni','salli thanpath kereemak','mudal thanpath kereemak']
intent3 = ['mata salli ganna oni','salli ganna oni','mata mudal ganna oni','mudal ganna oni','mata mudal ganna puluwnda','mata salli ganna puluwnda','mudal ganeemak','salli ganeemak']
intent4 = ['bill ekak gewanna oni','mata bill pathak gewanna oni','bill pathak gewanna oni','bill geweemak','bilak gewanna puluwnda']
intent5 = ['thawa ginumakata mudal maru karanna oni','thawa ginumakata mudal maru karanna puluwnda','wenath ginumakata mudal maru kereemak','wenath ginumakata salli maru kereemak','thawa ginumakata salli maru karanna oni','thawa ginumakata salli maru karanna puluwnda','wenath ginumakata salli maru kereemak']
intent6 = ['hara path geweemak karanna oni','mata hara path geweemak karanna oni','credit card ekata salli gewanna oni','mata credit card ekata salli gewanna oni']
intents = [intent1,intent2,intent3,intent4,intent5,intent6]

#Paths
fileString = "/home/ranula/Desktop/fyp/Model/sinhala_bank/wav/new2.wav"
accousticModel = "/home/ranula/Desktop/fyp/Model/sinhala_bank/model_parameters/sinhala_bank.ci_semi"
languageModel = "/home/ranula/Desktop/fyp/Model/sinhala_bank/etc/sinhala_bank.lm"
dictionary = "/home/ranula/Desktop/fyp/Model/sinhala_bank/etc/sinhala_bank.dic"

def voiceToText(filePath,accModel,langModel,dictionary):
    phrase=check_output("sudo pocketsphinx_continuous -infile "+filePath +" -hmm "+accModel+" -lm "+langModel+" -dict "+dictionary+" -logfn /dev/null",shell=True)
    phraseStripped = phrase.strip()
    return phraseStripped

def getIntent(text,Intents):
    intentNo = -1
    for intent in Intents:
        if text in intent:
            intentNo = (intents.index(intent))
    return intentNo    

print(getIntent(voiceToText(fileString,accousticModel,languageModel,dictionary),intents))