import sendgrid
import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

sg = sendgrid.SendGridClient(os.environ.get('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'))

# Basic Send Example

message = sendgrid.Mail()
message.add_to('<placetinder@gmail.com>')
message.set_subject('Sendgrid API test')
message.set_html('<b>testing!</b>')
message.set_text('testing!')
message.set_from('Place Tinder <placetinder@gmail.com')
status, msg = sg.send(message)
print status
print msg

"""
# SMTPAPI Basic Send Example

message = sendgrid.Mail()
message.add_substitution(':first_name', 'John')
message.smtpapi.add_to('John Doe <example@example.com>')
message.set_subject('Testing from the Python library using the SMTPAPI')
message.set_html('<b>:first_name, this was a successful test of using the SMTPAPI library!</b>')
message.set_text(':name, this was a successful test of using the SMTPAPI library!')
message.set_from('Jane Doe <example@example.com>')
status, msg = sg.send(message)
print status
print msg


# Template Engine Example
#    In the template editor, the subject is <%subject%> and the body is:
#
#    Hello :name,
#   
#    <%body%>
#
#    With Best Regards,
# 
#    Your Library Tester
# 
#    <%subject%> is replaced with the value in message.set_subject
#    <%body%> is replaced with the value in message.set_html and message.set_text
#    :name is replaced with the value in message.add_substitution

message = sendgrid.Mail()
message.add_filter('templates', 'enable', '1')
message.add_filter('templates', 'template_id', 'TEMPLATE-ALPHA-NUMERIC-ID')
message.add_substitution(':name', 'John')
message.add_to('John Doe <example@example.com')
message.set_subject('Testing from the Python library using the SMTPAPI')
message.set_html('<b>This was a successful test of using the SMTPAPI library!</b>')
message.set_text('This was a successful test of using the SMTPAPI library!')
message.set_from('Jane Doe <example@example.com>')
status, msg = sg.send(message)
print status
print msg
"""
