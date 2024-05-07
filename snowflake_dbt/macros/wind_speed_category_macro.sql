{% macro generate_wind_speed_category() %}
CASE
    WHEN wind_speed <= 4.5 THEN 'low'
    WHEN wind_speed >= 4.5 and wind_speed <= 8.0 THEN 'Average'
    WHEN wind_speed >= 8.0 THEN 'high'
ELSE 'Poor'
END AS wind_speed_category
  -- Using dbt's ref function to reference the films table
{% endmacro %}