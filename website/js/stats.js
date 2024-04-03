function getColor(value) {
    //values from 0 to 1
    if (value > 2.5) value = 2.5;
    var hue = ((2.5 - value) * 48).toString(10);
    return ["hsl(", hue, ",100%,50%)"].join("");
  }
  function myFunction() {
      var ssl_rtt = ssl_test;
      var tcp_rtt = tcp_test;
      var ip_address = "address_ip";
      var difference = Math.abs(ssl_rtt - tcp_rtt);
      //if ((ssl_rtt - 20000) > tcp_rtt) {
      var percent = difference/Math.max(ssl_rtt,tcp_rtt);
      var percent2 = difference/20000;
  
      document.getElementById("rttable").style.backgroundColor = getColor(percent2);
      /*if (percent2 >= 1){
          document.getElementById("rttable").style.backgroundColor = "#FFCCCB";
      }
      else {
          document.getElementById("rttable").style.backgroundColor = "#90EE90";
      }*/
      document.getElementById("c_percent").innerHTML = (percent2*100).toFixed(2) + "%";
      var user_agent = "http_user_agent";
      document.getElementById("http_user").innerHTML = user_agent;
      document.getElementById("ssl_rtt").innerHTML = ssl_rtt/1000 + 'ms';
      document.getElementById("ip_address").innerHTML = ip_address;
      var tcpi_state = tcpi_state_test;
      document.getElementById("tcpi_state").innerHTML = tcpi_state ?? 'null';
      var tcpi_ca_state = tcpi_ca_state_test;
      document.getElementById("tcpi_ca_state").innerHTML = tcpi_ca_state ?? 'null';
      var tcpi_retransmits = tcpi_retransmits_test;
      document.getElementById("tcpi_retransmits").innerHTML = tcpi_retransmits ?? 'null';
      var tcpi_probes = tcpi_probes_test;
      document.getElementById("tcpi_probes").innerHTML = tcpi_probes ?? 'null';
      var tcpi_backoff = tcpi_backoff_test;
      document.getElementById("tcpi_backoff").innerHTML = tcpi_backoff ?? 'null';
      var tcpi_options = tcpi_options_test;
      document.getElementById("tcpi_options").innerHTML = tcpi_options ?? 'null';
      var tcpi_snd_wscale = tcpi_snd_wscale_test;
      document.getElementById("tcpi_snd_wscale").innerHTML = tcpi_snd_wscale ?? 'null';
      var tcpi_rcv_wscale = tcpi_rcv_wscale_test;
      document.getElementById("tcpi_rcv_wscale").innerHTML = tcpi_rcv_wscale ?? 'null';
      var tcpi_delivery_rate_app_limited = tcpi_delivery_rate_app_limited_test;
      document.getElementById("tcpi_delivery_rate_app_limited").innerHTML = tcpi_delivery_rate_app_limited ?? 'null';
      var tcpi_fastopen_client_fail = tcpi_fastopen_client_fail_test;
      document.getElementById("tcpi_fastopen_client_fail").innerHTML = tcpi_fastopen_client_fail ?? 'null';
      var tcpi_rto = tcpi_rto_test;
      document.getElementById("tcpi_rto").innerHTML = tcpi_rto ?? 'null';
      var tcpi_ato = tcpi_ato_test;
      document.getElementById("tcpi_ato").innerHTML = tcpi_ato ?? 'null';
      var tcpi_snd_mss = tcpi_snd_mss_test;
      document.getElementById("tcpi_snd_mss").innerHTML = tcpi_snd_mss ?? 'null';
      var tcpi_rcv_mss = tcpi_rcv_mss_test;
      document.getElementById("tcpi_rcv_mss").innerHTML = tcpi_rcv_mss ?? 'null';
      var tcpi_unacked = tcpi_unacked_test;
      document.getElementById("tcpi_unacked").innerHTML = tcpi_unacked ?? 'null';
      var tcpi_sacked = tcpi_sacked_test;
      document.getElementById("tcpi_sacked").innerHTML = tcpi_sacked ?? 'null';
      var tcpi_lost = tcpi_lost_test;
      document.getElementById("tcpi_lost").innerHTML = tcpi_lost ?? 'null';
      var tcpi_retrans = tcpi_retrans_test;
      document.getElementById("tcpi_retrans").innerHTML = tcpi_retrans ?? 'null';
      var tcpi_fackets = tcpi_fackets_test;
      document.getElementById("tcpi_fackets").innerHTML = tcpi_fackets ?? 'null';
      var tcpi_last_data_sent = tcpi_last_data_sent_test;
      document.getElementById("tcpi_last_data_sent").innerHTML = tcpi_last_data_sent ?? 'null';
      var tcpi_last_ack_sent = tcpi_last_ack_sent_test;
      document.getElementById("tcpi_last_ack_sent").innerHTML = tcpi_last_ack_sent ?? 'null';
      var tcpi_last_data_recv = tcpi_last_data_recv_test;
      document.getElementById("tcpi_last_data_recv").innerHTML = tcpi_last_data_recv ?? 'null';
      var tcpi_last_ack_recv = tcpi_last_ack_recv_test;
      document.getElementById("tcpi_last_ack_recv").innerHTML = tcpi_last_ack_recv ?? 'null';
      var tcpi_pmtu = tcpi_pmtu_test;
      document.getElementById("tcpi_pmtu").innerHTML = tcpi_pmtu ?? 'null';
      var tcpi_rcv_ssthresh = tcpi_rcv_ssthresh_test;
      document.getElementById("tcpi_rcv_ssthresh").innerHTML = tcpi_rcv_ssthresh ?? 'null';
      var tcpi_rtt = tcpi_rtt_test;
      document.getElementById("tcpi_rtt").innerHTML = tcpi_rtt/1000 + 'ms' ?? 'null';
      var tcpi_rttvar = tcpi_rttvar_test;
      document.getElementById("tcpi_rttvar").innerHTML = tcpi_rttvar/1000 + 'ms' ?? 'null';
      var tcpi_snd_ssthresh = tcpi_snd_ssthresh_test;
      document.getElementById("tcpi_snd_ssthresh").innerHTML = tcpi_snd_ssthresh ?? 'null';
      var tcpi_snd_cwnd = tcpi_snd_cwnd_test;
      document.getElementById("tcpi_snd_cwnd").innerHTML = tcpi_snd_cwnd ?? 'null';
      var tcpi_advmss = tcpi_advmss_test;
      document.getElementById("tcpi_advmss").innerHTML = tcpi_advmss ?? 'null';
      var tcpi_reordering = tcpi_reordering_test;
      document.getElementById("tcpi_reordering").innerHTML = tcpi_reordering ?? 'null';
      var tcpi_rcv_rtt = tcpi_rcv_rtt_test;
      document.getElementById("tcpi_rcv_rtt").innerHTML = tcpi_rcv_rtt ?? 'null';
      var tcpi_rcv_space = tcpi_rcv_space_test;
      document.getElementById("tcpi_rcv_space").innerHTML = tcpi_rcv_space ?? 'null';
      var tcpi_total_retrans = tcpi_total_retrans_test;
      document.getElementById("tcpi_total_retrans").innerHTML = tcpi_total_retrans ?? 'null';
      var tcpi_pacing_rate = tcpi_pacing_rate_test;
      document.getElementById("tcpi_pacing_rate").innerHTML = tcpi_pacing_rate ?? 'null';
      var tcpi_max_pacing_rate = tcpi_max_pacing_rate_test;
      document.getElementById("tcpi_max_pacing_rate").innerHTML = tcpi_max_pacing_rate ?? 'null';
      var tcpi_bytes_acked = tcpi_bytes_acked_test;
      document.getElementById("tcpi_bytes_acked").innerHTML = tcpi_bytes_acked ?? 'null';
      var tcpi_bytes_received = tcpi_bytes_received_test;
      document.getElementById("tcpi_bytes_received").innerHTML = tcpi_bytes_received ?? 'null';
      var tcpi_segs_out = tcpi_segs_out_test;
      document.getElementById("tcpi_segs_out").innerHTML = tcpi_segs_out ?? 'null';
      var tcpi_segs_in = tcpi_segs_in_test;
      document.getElementById("tcpi_segs_in").innerHTML = tcpi_segs_in ?? 'null';
      var tcpi_notsent_bytes = tcpi_notsent_bytes_test;
      document.getElementById("tcpi_notsent_bytes").innerHTML = tcpi_notsent_bytes ?? 'null';
      var tcpi_min_rtt = tcpi_min_rtt_test;
      document.getElementById("tcpi_min_rtt").innerHTML = tcpi_min_rtt/1000 + 'ms' ?? 'null';
      var tcpi_data_segs_in = tcpi_data_segs_in_test;
      document.getElementById("tcpi_data_segs_in").innerHTML = tcpi_data_segs_in ?? 'null';
      var tcpi_data_segs_out = tcpi_data_segs_out_test;
      document.getElementById("tcpi_data_segs_out").innerHTML = tcpi_data_segs_out ?? 'null';
      var tcpi_delivery_rate = tcpi_delivery_rate_test;
      document.getElementById("tcpi_delivery_rate").innerHTML = tcpi_delivery_rate ?? 'null';
      var tcpi_busy_time = tcpi_busy_time_test;
      document.getElementById("tcpi_busy_time").innerHTML = tcpi_busy_time ?? 'null';
      var tcpi_rwnd_limited = tcpi_rwnd_limited_test;
      document.getElementById("tcpi_rwnd_limited").innerHTML = tcpi_rwnd_limited ?? 'null';
      var tcpi_sndbuf_limited = tcpi_sndbuf_limited_test;
      document.getElementById("tcpi_sndbuf_limited").innerHTML = tcpi_sndbuf_limited ?? 'null';
      var tcpi_delivered = tcpi_delivered_test;
      document.getElementById("tcpi_delivered").innerHTML = tcpi_delivered ?? 'null';
      var tcpi_delivered_ce = tcpi_delivered_ce_test;
      document.getElementById("tcpi_delivered_ce").innerHTML = tcpi_delivered_ce ?? 'null';
      var tcpi_bytes_sent = tcpi_bytes_sent_test;
      document.getElementById("tcpi_bytes_sent").innerHTML = tcpi_bytes_sent ?? 'null';
      var tcpi_bytes_retrans = tcpi_bytes_retrans_test;
      document.getElementById("tcpi_bytes_retrans").innerHTML = tcpi_bytes_retrans ?? 'null';
      var tcpi_dsack_dups = tcpi_dsack_dups_test;
      document.getElementById("tcpi_dsack_dups").innerHTML = tcpi_dsack_dups ?? 'null';
      var tcpi_reord_seen = tcpi_reord_seen_test;
      document.getElementById("tcpi_reord_seen").innerHTML = tcpi_reord_seen ?? 'null';
      var tcpi_rcv_ooopack = tcpi_rcv_ooopack_test;
      document.getElementById("tcpi_rcv_ooopack").innerHTML = tcpi_rcv_ooopack ?? 'null';
      //var tcpi_ack = tcpi_ack_test;
      //document.getElementById("tcpi_ack").innerHTML = tcpi_ack ?? 'null';
      //var tcpi_tls_hello = tcpi_tls_hello_test;
      document.getElementById("tcpi_snd_wnd").innerHTML = tcpi_snd_wnd ?? 'null';
      var tcpi_snd_wnd = tcpi_snd_wnd_test;
      document.getElementById("tcpi_snd_wnd").innerHTML = tcpi_snd_wnd ?? 'null';
      var percentage = (ssl_rtt - tcp_rtt);
      document.getElementById("percent").innerHTML = Math.abs(percentage)/1000 + 'ms';
  
      // Figures out User Agent OS
      const osKeywords = ['windows', 'macintosh', 'linux', 'iphone', 'android'];
      let userOS = 'other';
      osKeywords.forEach(keyword => {
          if (user_agent.toLowerCase().includes(keyword)) {
              userOS = keyword.charAt(0).toUpperCase() + keyword.slice(1);
          }
      if (userOS.toLowerCase() == 'iphone' || userOS.toLowerCase() == 'macintosh') {
          userOS = 'macintosh/IOS';
      }
      });
  
      // Establish OS TCP details
      var operatingSystems = [
          { os: "windows", tcpinfo_options: 6, tcpinfo_snd_wscale: 8, tcpinfo_snd_wnd_min: 130000, tcpinfo_snd_wnd_max: 132000 },
          { os: "macintosh/IOS", tcpinfo_options: 6, tcpinfo_snd_wscale: 6, tcpinfo_snd_wnd_min: 130000, tcpinfo_snd_wnd_max: 132000 },
          { os: "macintosh/IOS", tcpinfo_options: 6, tcpinfo_snd_wscale: 6, tcpinfo_snd_wnd_min: 261000, tcpinfo_snd_wnd_max: 263000 },
          { os: "macintosh/IOS", tcpinfo_options: 7, tcpinfo_snd_wscale: 6, tcpinfo_snd_wnd_min: 130000, tcpinfo_snd_wnd_max: 132000 },
          { os: "macintosh/IOS", tcpinfo_options: 7, tcpinfo_snd_wscale: 6, tcpinfo_snd_wnd_min: 261000, tcpinfo_snd_wnd_max: 263000 },
          { os: "linux", tcpinfo_options: 6, tcpinfo_snd_wscale: 7, tcpinfo_snd_wnd_min: 24100, tcpinfo_snd_wnd_max: 64200 },
          { os: "linux", tcpinfo_options: 7, tcpinfo_snd_wscale: 7, tcpinfo_snd_wnd_min: 24100, tcpinfo_snd_wnd_max: 64200 },
          { os: "android", tcpinfo_options: 6, tcpinfo_snd_wscale: 10, tcpinfo_snd_wnd_min: 65000, tcpinfo_snd_wnd_max: 100000 },
          { os: "android", tcpinfo_options: 6, tcpinfo_snd_wscale: 8, tcpinfo_snd_wnd_min: 65000, tcpinfo_snd_wnd_max: 100000 },
      ];
  
      // Calculate TCP OS based on TCP parameters
      var TCPuserOS = 'other';
      operatingSystems.forEach(os => {
          if (os.tcpinfo_options === tcpi_options &&
              os.tcpinfo_snd_wscale === tcpi_snd_wscale &&
              os.tcpinfo_snd_wnd_min < tcpi_snd_wnd &&
              os.tcpinfo_snd_wnd_max > tcpi_snd_wnd) {
              TCPuserOS = os.os;
          }
      });
  
      document.getElementById("tcpOS").innerHTML = TCPuserOS;
  
      // Set the background color of the TCP table
      if (userOS.toLowerCase() === TCPuserOS.toLowerCase()) {
          document.getElementById("tcptable").style.backgroundColor = "#90EE90"; // Green
      } else {
          document.getElementById("tcptable").style.backgroundColor = "#FFCCCB"; // Red
      }
  }
  