## 完成

<table>
    <thead>
        <tr style="background-color:green;">
            <th align="left"><font color="white">No.</font></th>
            <th align="left"><font color="white">Title</font></th>
            <th align="left"><font color="white">Tag</font></th>
            <th align="left"><font color="white">Level</font></th>
            <th align="left"><font color="white">Done</font></th>
        </tr>
    </thead>
    <tbody>
        {% for k, v in problems.items() -%}
        {% if k in finished %}<tr bgcolor="lightgreen">{% else %}<tr>{% endif %}
            <td>{{k}}</td>
            <td><a href="{{links[k]['href']}}">{{links[k]['cn_title']}}</a></td>
            <td>{% if k in tags %}{{tags[k]}}{% endif %}</td>
            {% if links[k]["level"] == "困难" -%}
            <td><font color="red">{{links[k]["level"]}}</font></td>
            {%- elif links[k]["level"] == "中等" -%}
            <td><font color="green">{{links[k]["level"]}}</font></td>
            {%- else -%}
            <td><font color="blue">{{links[k]["level"]}}</font></td>
            {%- endif %}
            <td>{% if k in finished %}{{"✓"}}{% else %}{{""}}{% endif %}</td>
        </tr>
        {% endfor -%}
    </tbody>
</table>