<thead>
            <tr>
                <th>Train_no</th>
                <th>Name</th>
                <th>Place From</th>
                <th>Place To</th>
                <th>Date</th>
                <th>Time</th>
                <th>Gender</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Amount</th>
                <th>Image</th>
            </tr>
        </thead>
        <tbody style="text-align: center;">
            {% for record in records %}
            <tr>
                <td>{{ record.train_no }}</td>
                <td>{{ record.uname }}</td>
                <td>{{ record.place1 }}</td>
                <td>{{ record.place2 }}</td>
                <td>{{ record.dates }}</td>
                <td>{{ record.times }}</td>
                <td>{{ record.gender }}</td>
                <td>{{ record.mobile }}</td>
                <td>{{ record.emailid }}</td>
                <td>{{ record.amount }}</td>
                <td>
                    {% if record.image %}
                    <img src="{{ url_for('static', filename='checked.jpeg') }}" alt="Image" style="width: 20px; height: auto;">
                    {% else %}
                    <img src="{{ url_for('static', filename='wrong-cross-symbol-isolated-white-background-d-render-wrong-cross-symbol-isolated-115034877.jpg') }}" alt="kjnd"  style="width: 20px; height: auto;">
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% else %}
    <p>No records found for the email: {{ email }}</p>
    {% endif %}