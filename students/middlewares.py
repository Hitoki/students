from django.db import connection
from django.template import Template, Context


class TimeSQLRe:

    def process_response(self, request, response):

        content_types = ('text/plain', 'text/html')

        if request.META['CONTENT_TYPE'] not in content_types:
            return response

        time = sum([float(q['time']) for q in connection.queries])

        template = Template('''<div class="debug">
                <p>время выполнения запроса: {{ time }}</p>
                <p>количество sql запросов: {{ count }}</p>
            <div>
            ''')

        renderred_template = template.render(Context(dict(time=time, count=len(connection.queries))))


        content = response.content.decode('utf-8')

        body = '</body>'
        body_position = content.find(body)
        content = content[:body_position] + renderred_template + content[body_position:]
        
        response.content = content.encode('utf-8')

        return  response