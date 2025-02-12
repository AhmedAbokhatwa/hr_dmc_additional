# from hrms.hrms.payroll.doctype.payroll_entry.payroll_entry import PayrollEntry
# # should_add_component_to_accrual_jv


# PayrollEntry.should_add_component_to_accrual_jv()

# def should_add_component_to_accrual_jv(self, component_type: str, item: dict) -> bool:
#   add_component_to_accrual_jv = True
#   if component_type == "earnings":
#     is_flexible_benefit, only_tax_impact = frappe.get_cached_value(
#       "Salary Component", item["salary_component"], ["statistical_component","is_flexible_benefit", "only_tax_impact"]
#     )
#     if cint(is_flexible_benefit) and cint(only_tax_impact):
#       add_component_to_accrual_jv = False
    
#   return 

from hrms.payroll.doctype.payroll_entry.payroll_entry import PayrollEntry
import frappe
from frappe.utils import cint

class CustomPayroll(PayrollEntry):
    
    # Overriding the method from the base class
    def should_add_component_to_accrual_jv(self, component_type: str, item: dict) -> bool:
        add_component_to_accrual_jv = True
        do_not_include_in_total, is_flexible_benefit, only_tax_impact = frappe.get_cached_value(
            "Salary Component", item["salary_component"], ["do_not_include_in_total", "is_flexible_benefit", "only_tax_impact"]
        )
        if cint(do_not_include_in_total):
            add_component_to_accrual_jv = False   
        if component_type == "earnings":
            # Check if it's a flexible benefit and only has a tax impact
            if cint(is_flexible_benefit) and cint(only_tax_impact):
                add_component_to_accrual_jv = False

        return add_component_to_accrual_jv
