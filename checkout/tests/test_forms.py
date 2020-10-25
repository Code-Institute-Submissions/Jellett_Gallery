from django.test import TestCase
from django import forms
from django.contrib.auth.models import User
from checkout.forms import OrderForm


class TestOrderForm(TestCase):

    def setUp(self):
        self.form = OrderForm()

    def test_full_name_label(self):
        self.assertEqual(self.form.fields['full_name'].label, 'Full name')

    def test_email_label(self):
        self.assertEqual(self.form.fields["email"].label, 'Email Address')

    def test_phone_number_label(self):
        self.assertEqual(self.form.fields['phone_number'].label, "Phone number")

    def test_postcode_label(self):
        self.assertEqual(self.form.fields["postcode"].label, "Postal Code")

    def test_town_or_city_label(self):
        self.assertEqual(self.form.fields["town_or_city"].label, "Town or city")

    def test_street_address1_label(self):
        self.assertEqual(self.form.fields["street_address1"].label, "Street Address 1")

    def test_street_address2_label(self):
        self.assertEqual(self.form.fields["street_address2"].label, "Street Address 2")

    def test_country_label(self):
        self.assertEqual(self.form.fields["county"].label, "County or Locality")



# class TestMakePaymentForm(TestCase):

#     def setUp(self):
#         self.form = MakePaymentForm()

#     def test_credit_card_number_label(self):
#         self.assertEqual(self.form.fields["credit_card_number"].label, "Credit card number")

#     def test_cvv_label(self):
#         self.assertEqual(self.form.fields["cvv"].label, "Security code (CVV)")

#     def test_expiry_month_label(self):
#         self.assertEqual(self.form.fields["expiry_month"].label, "Month")

#     def test_expiry_year_label(self):
#         self.assertEqual(self.form.fields["expiry_year"].label, "Year")