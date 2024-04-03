import os

def create_file(filename, data):
  """Creates a new file with the given name and writes the given data to it."""
  if os.path.exists(filename):
    os.remove(filename)
  with open(filename, "w") as f:
    f.write(data)

def generate_auto_unix_c_data(variable_name: str):
  """Generates the data to be appended to the `auto.unix.c` file for the given variable name."""
  return """
ngx_feature="{name}"
ngx_feature_name="NGX_HAVE_{name}"
ngx_feature_run=no
ngx_feature_incs="#include <sys/socket.h>
                  #include <netinet/in.h>
                  #include <netinet/tcp.h>"
ngx_feature_path=
ngx_feature_libs=
ngx_feature_test="socklen_t optlen = sizeof(struct tcp_info);
                  struct tcp_info ti;
                  ti.{variable} = 0;
                  getsockopt(0, IPPROTO_TCP, TCP_INFO, &ti, &optlen)"
. auto/feature
  """.format(name=variable_name.upper(), variable=variable_name)

def generate_http_variables1_c_data(variable_name, variable_number):
  statement = "#if (NGX_HAVE_{variable_name})\n".format(variable_name=variable_name.upper())
  end = "#endif\n"
  """Generates the data to be appended to the `http.variables1.c` file for the given variable name and variable number."""
  return statement + """    {{ ngx_string("tcpinfo_{variable_name}"), NULL, ngx_http_variable_tcpinfo,      {variable_number}, NGX_HTTP_VAR_NOCACHEABLE, 0 }},
""".format(variable_name=variable_name, variable_number=variable_number).replace("tcpi_","") + end

def generate_http_variables2_c_data(variable_name, variable_number):
  """Generates the data to be appended to the `http.variables2.c` file for the given variable name and variable number."""
  statement = "\n#if (NGX_HAVE_{variable_name})\n".format(variable_name=variable_name.upper())
  end = "#endif"
  return statement + """    case {variable_number}:
        value = ti.{variable_name};        
        break;
""".format(variable_name=variable_name, variable_number=variable_number) + end

def generate_csv_log_style(variable_name):
  return """$tcpinfo_{variable_name},""".format(variable_name=variable_name).replace("tcpi_","")

def generate_html_exposure(variable_name):
  name = str(variable_name).replace("tcpi_","").capitalize()
  return """<h2>{name}: <span id="tcpinfo_{variable_name}"></span></h2>
  """.format(variable_name=variable_name, name=name).replace("tcpi_","")

def generate_sub_filter(variable_name):
  return """sub_filter '{variable_name}_test' ${variable_name};
  """.format(variable_name=variable_name)
def generate_js(variable_name):
  return """  var {variable_name} = {variable_name}_test;
    document.getElementById("{variable_name}").innerHTML = {variable_name};
""".format(variable_name=variable_name)

def main():
  # Get the comma-separated list of variables from the user.
  variable_list = input("Enter a comma-separated list of variables: ")

  # Generate the data for each file.
  auto_unix_c_data = ""
  http_variables1_c_data = ""
  http_variables2_c_data = ""
  csv_log_format = ""
  html = ""
  sub_filter = ""
  js = ""

  variable_number = 0
  for variable_name in variable_list.split(","):
    auto_unix_c_data += generate_auto_unix_c_data(variable_name)
    http_variables1_c_data += generate_http_variables1_c_data(variable_name, variable_number)
    http_variables2_c_data += generate_http_variables2_c_data(variable_name, variable_number)
    csv_log_format += generate_csv_log_style(variable_name)
    html += generate_html_exposure(variable_name)
    sub_filter += generate_sub_filter(variable_name)
    js += generate_js(variable_name)


    variable_number += 1

  # Create the files and append the data to them.
  create_file("auto.unix.c", auto_unix_c_data)
  create_file("http.variables1.c", http_variables1_c_data)
  create_file("http.variables2.c", http_variables2_c_data)
  create_file("csv.log.format.txt", csv_log_format[:-1])
  create_file("html.html", html)
  create_file("sub_filter.txt", sub_filter)
  create_file("js.js", js)

if __name__ == "__main__":
  main()