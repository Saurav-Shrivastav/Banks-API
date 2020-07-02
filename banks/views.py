from django.shortcuts import render
from django.views import View
import csv
from threading import Thread
from django.contrib import messages
from banks.models import Bank, Branch


def upload(reader):
    for row in reader:
        bank_id = row.get("bank_id")
        ifsc = row.get("ifsc")
        branch = row.get("branch")
        address = row.get("address")
        city = row.get("city")
        district = row.get("district")
        state = row.get("state")
        print("IFSC-- {}".format(ifsc))
        if not ifsc:
            break
        bank_object, created = Bank.objects.get_or_create(id=bank_id)
        branch_defaults = {
            "branch": branch,
            "bank_id": bank_object,
            "address": address,
            "city": city,
            "district": district,
            "state": state,
        }

        branch_object, created = Branch.objects.update_or_create(
            ifsc=ifsc, defaults=branch_defaults
        )
        if created:
            print("row created{}".format(branch_defaults))

        # print("No of Rows imported - {} - {} ".format(count, branch_defaults))


# Create your views here.
class ImportView(View):
    def get(self, request):
        return render(request, "import.html")

    def post(self, request):
        csv_file = request.FILES.get("csv_file")
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)
        # ifsc_list = list(Branch.objects.values_list('ifsc', flat=True))

        messages.success(request, "rows imported.")
        thread = Thread(target=upload, kwargs={"reader": reader})
        thread.start()
        return render(request, "import.html")
