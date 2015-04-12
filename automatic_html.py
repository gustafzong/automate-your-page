"""def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text"""

def generate_HTML_for_a_layer(title_layer, description_layer, layer):
    str_layer=str(layer)
    layer_start = '''
<div class="chapter_layer_'''+str_layer+'">'
    layer_title='''
    <h'''+str_layer+'>'+title_layer+'</h'+str_layer+'''>
    '''
    result=layer_start+layer_title+description_layer
    return result



def finishDiv(htmlCodeLackDiv):
    result=htmlCodeLackDiv+'''
    </div>'''
    return result


# My input list is like 
# [titleLayer1, descriptionLayer1, 
# [
# [titleLayer2_1, descriptionLayer2_1],
# [titleLayer2_2, descriptionLayer2_2]
# ]]
def make_HTML(concept):
    title_layer_1 = concept[0]
    description_layer_1 = concept[1]
    htmlCode=generate_HTML_for_a_layer(title_layer_1, description_layer_1, 1)
    if len(concept)>2:
        for conceptLayer2 in concept[2]:
            title_layer_2 = conceptLayer2[0]
            description_layer_2 = conceptLayer2[1]
            htmlCode=finishDiv(htmlCode+generate_HTML_for_a_layer(title_layer_2, description_layer_2, 2))
    return finishDiv(htmlCode)

LIST_OF_CONCEPTS = [ 
["Python", 
"Python is a programming language. Unlike HTML and CSS which can only be used for the description of web pages, Python could serve a variety of purposes, for instance, automatically generate HTML code.",
[
["Grammar","""Every programming language has its own grammar. Here, the grammar means the way to express our command which could enable the computer to understand it.
One crucial part of grammar is its structure of expression. This video provide a good explanation of the rule for constructing a valid expression."""],
['Variable', '''We can give names to values to let them become a variable. By allowing us to store and modify the value, variable enable us to complete more complicated tasks. More over, we can simply give variables meaningful names to increase the readability of our code. To define a variable and assign it to a value, we can write code like "a=3" in Python, which means we create a variable a and let its value to be 3 and the operator "=" here means "takes the value of".'''], 
['Operator', '''There are many operators in Python, such as arithmetic operators "+", "-", "*" and "/". One important point is that one operators could have different meanings in different context, for example, when "+" appears between two numbers, it means plus, and when it appears between two Strings, it means concatenation.'''], 
['Decision And Loop', '''We can put a segment of code into a if branch in order to make a decision which part of code should be executed. We can also put something into a loop to repeat doing the same stuff. The following videos explain how to construct a if branch and a while loop.

We can also use a for loop to iterate the elements in a list and do something to them.

We can build code to realize a complex task by using these structure. 
'''],
['Function', '''A function is like a segment of code which could be called by its name. By defining and calling function, we can significantly avoid repetition and increase the readability of our code.

A function can take input and give output. A function ends and sends the output to where it is called when it meet the keyword return

Here is an example of defining and calling a function:

defining a function:

def calculateSum(input1, input2): 

    output=input1+input2 

    return output



calling a function:

print calculateSum(1,2) 

It should print 3.



If a function does not have output, it is not necessarily a useless function, because the modification it made may still be there after it finishes. For example, the modification on an array passed in will not be canceled after the function finishes.''']]]]

def make_HTML_for_many_concepts(list_of_concepts):
    result=""
    for concept in list_of_concepts:
        result=result+make_HTML(concept)
    return result

print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)