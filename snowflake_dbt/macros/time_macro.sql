{% macro generate_time_format() %}
cast(substr(date,12) as time) 
AS time_format
  -- Using dbt's ref function to reference the films table
{% endmacro %}