$("#user_type").change(function() {
			if ($(this).val() == "hospital") {
				$('#hospital_name').show();
				$('#h_name').attr('required','');
				$('#h_name').attr('data-error', 'This field is required.');
				$('#vendor_name').hide();
				$('#v_name').removeAttr('required');
				$('#v_name').removeAttr('data-error');
				$('#about_us_div').hide();
				$('#v_about_us').removeAttr('required');
				$('#v_about_us').removeAttr('data-error');
			} else if ($(this).val() == "vendor") {
				$('#vendor_name').show();
				$('#v_name').attr('required','');
				$('#v_name').attr('data-error', 'This field is required.');
				$('#about_us_div').show();
				$('#v_about_us').attr('required','');
				$('#v_about_us').attr('data-error', 'This field is required.');
				$('#hospital_name').hide();
				$('#h_name').removeAttr('required');
				$('#h_name').removeAttr('data-error');
			}
			else if($(this).val() == "none"){
				$('#hospital_name').hide();
				$('#h_name').removeAttr('required');
				$('#h_name').removeAttr('data-error');
				$('#vendor_name').hide();
				$('#v_name').removeAttr('required');
				$('#v_name').removeAttr('data-error');
				$('#about_us_div').hide();
				$('#v_about_us').removeAttr('required');
				$('#v_about_us').removeAttr('data-error');
			}
		});
		$("#user_type").trigger("change");
		
