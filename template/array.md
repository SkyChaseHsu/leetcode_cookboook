## 完成

<table>
    <thead>
        <tr style="background-color:green;">
            <th>No.</th>
            <th>Title</th>
            <th>Link</th>
            <th>Done</th>
        </tr>
    </thead>
    <tbody>
        {% for k, v in problems.items() -%}
        {% if k in finished %}<tr bgcolor="lightgreen">{% else %}<tr>{% endif %}
            <td>{{k}}</td>
            <td>{{v}}</td>
            <td>{% if k in finished %}<a href="https://leetcode-cn.com/problems/{{finished[k]}}/">Go</a>{% else %}{{""}}{% endif %}</td>
            <td>{% if k in finished %}{{"✓"}}{% else %}{{""}}{% endif %}</td>
        </tr>
        {% endfor -%}
    </tbody>
</table>