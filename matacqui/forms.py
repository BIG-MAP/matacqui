# -*- coding: utf-8 -*-
import uuid

import IPython.display
import ipywidgets as wdg

import mincepy
import mincepy.fields

__all__ = ('MaterialsOrder', 'MaterialsAcquisitionForm', 'form_data_schema')


class ContactDetails(mincepy.SimpleSavable):
    """Database storable class representing a person's contact details"""
    TYPE_ID = uuid.UUID('7d2e1cf5-6c75-4b85-9fe3-46c70e680e69')

    name = mincepy.field()
    email = mincepy.field()
    institution = mincepy.field()
    address = mincepy.field()
    task = mincepy.field()
    work_package = mincepy.field()

    def get_html(self) -> str:
        lines = ['<p><u>Contact Information</u>']

        for field_name in mincepy.fields.get_fields(type(self)).keys():
            lines.append(f'{field_name}:\t {getattr(self, field_name)}')

        lines.append('</p>')

        return '<br/>\n'.join(lines)


class OrderDetails(mincepy.SimpleSavable):
    """Database storable class representing details of an order"""
    TYPE_ID = uuid.UUID('30b8797f-1d23-4ed2-b041-790f1be013d1')

    component = mincepy.field()
    category = mincepy.field()
    subcategory = mincepy.field()
    specifications = mincepy.field()
    amounts = mincepy.field()

    def get_html(self) -> str:
        lines = [
            '<p><u>Item</u>', self.component + ' : ' + self.category + ' : ' + self.subcategory,
            '</p>'
            '<p><u>Specifications</u>'
        ]
        # Order specifications
        for key, value in self.specifications.items():
            lines.append(key + ': ' + str(value))
        lines.append('</p>')

        # Order amounts
        lines.append('<p><u>Order</u>')
        for key, value in self.amounts.items():
            lines.append(key + ': ' + str(value))
        lines.append('</p>')

        return '</br>\n'.join(lines)


class MaterialsOrder(mincepy.SimpleSavable):
    TYPE_ID = uuid.UUID('59d32bcf-2e1d-41bd-900c-872977331937')

    contact = mincepy.field()
    order = mincepy.field()

    def __init__(self, contact: ContactDetails, order: OrderDetails):
        super().__init__()
        self.contact = contact
        self.order = order

    def get_html(self) -> str:
        lines = [self.contact.get_html(), self.order.get_html()]
        return '<br/>\n'.join(lines)


form_data_schema = {
    'Anode': {
        'Graphite': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            }
        },
        'Silicon': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            }
        },
        'Silicon/graphite': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Sheet area M13-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            },
            'special': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Ciditec',
                    'Contact': 'Elixabete Ayerbe',
                    'Contact Email': 'eayerbe@cidetec.es'
                },
                'input': {
                    'Request': ''
                }
            }
        },
        'Lithium metal': {
            'sheet': {
                'properties': {
                    'ID': '',
                    'Supplier': 'HONJO'
                },
                'input': {
                    'Sheet area [cm^2]': 0
                }
            }
        }
    },
    'Cathode': {
        'NMC811': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Umicore',
                    'Contact': 'Jeremie Auvergniot',
                    'Contact Email': 'Jeremie.Auvergniot@eu.umicore.com'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Umicore',
                    'Contact': 'Jeremie Auvergniot',
                    'Contact Email': 'Jeremie.Auvergniot@eu.umicore.com'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            }
        },
        'LiNiO2': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'BASF',
                    'Contact': 'Pascal Hartmann',
                    'Contact Email': 'pascal.hartmann@basf.com'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Standard': '0.5 m^2 single side coating',
                    'Supplier': 'BASF',
                    'Contact': 'Pascal Hartmann',
                    'Contact Email': 'pascal.hartmann@basf.com'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M24-36 [cm^2]': 0
                }
            }
        },
        'NMC622': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Umicore',
                    'Contact': 'Jeremie Auvergniot',
                    'Contact Email': 'Jeremie.Auvergniot@eu.umicore.com'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Umicore',
                    'Contact': 'Jeremie Auvergniot',
                    'Contact Email': 'Jeremie.Auvergniot@eu.umicore.com'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            }
        },
        'LNMO': {
            'powder': {
                'properties': {
                    'ID': '',
                    'Supplier': 'BASF',
                    'Contact': 'Pascal Hartmann',
                    'Contact Email': 'pascal.hartmann@basf.com'
                },
                'input': {
                    'Quantity M3-12 [g]': 0,
                    'Quantity M13-24 [g]': 0,
                    'Quantity M25-36 [g]': 0
                }
            },
            'electrode': {
                'properties': {
                    'ID': '',
                    'Supplier': 'BASF',
                    'Contact': 'Pascal Hartmann',
                    'Contact Email': 'pascal.hartmann@basf.com'
                },
                'input': {
                    'Sheet area M3-12 [cm^2]': 0,
                    'Sheet area M13-24 [cm^2]': 0,
                    'Sheet area M25-36 [cm^2]': 0,
                    'Thickness [um]': 0,
                    'Loading [mAh/cm^2]': 0
                }
            },
            'special request': {
                'properties': {
                    'ID': '',
                    'Supplier': 'BASF',
                    'Contact': 'Pascal Hartmann',
                    'Contact Email': 'pascal.hartmann@basf.com'
                },
                'input': {
                    'Request': '',
                    'Amount [units]': ''
                }
            }
        }
    },
    'Electrolyte': {
        'Formulation': {
            'LP30': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP37': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP40': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP47': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP50': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP57': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP57 + 2% VC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'LP57 + 10%% FEC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            }
        },
        'Component': {
            'LiPF6': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [g]': [50, 500]
                }
            },
            'LiTFSI': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm',
                    'Supplier': 'Solvay',
                    'Contact': 'Marc-David Braida',
                    'Contact Email': 'marc-david.braida@solvay.com'
                },
                'input': {
                    'Quantity [g]': [50, 500]
                }
            },
            'LiFSI': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm',
                    'Supplier': 'Solvay',
                    'Contact': 'Marc-David Braida',
                    'Contact Email': 'marc-david.braida@solvay.com'
                },
                'input': {
                    'Quantity [g]': [50, 500]
                }
            },
            'EC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [g]': [50, 500]
                }
            },
            'DMC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'DEC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'EMC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'VC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            },
            'FEC': {
                'properties': {
                    'ID': '',
                    'Purity': 'Battery grade',
                    'Water content': '< 20 ppm',
                    'Supplier': 'Solvay',
                    'Contact': 'Marc-David Braida',
                    'Contact Email': 'marc-david.braida@solvay.com'
                },
                'input': {
                    'Quantity [L]': [1]
                }
            }
        },
        'Fluorinated solvent': {
            'solvent': {
                'properties': {
                    'ID': '',
                    'Supplier': 'Solvay'
                },
                'input': {
                    'Request': '',
                    'Volume [L]': [1]
                }
            }
        }
    },
    'Separator': {
        'Celgard 2500': {
            'Porosity 53%': {
                'properties': {
                    'ID': '',
                    'Thickness': '25 um',
                    'Porosity': '53%',
                    'Order contact': 'Mario Giovagnoli'
                },
                'input': {
                    'Sheet area [cm^2]': 0
                }
            }
        },
        'Other': {
            'Special request': {
                'properties': {
                    'ID': ''
                },
                'input': {
                    'Request': '',
                    'Sheet area [cm^2]': 0
                }
            }
        }
    }
}


class ContactInfoSubapp:
    """Contact information sub app"""

    def __init__(self):
        # subapp attributes
        self.widget = {}
        self.widget_box = {}
        self.interface = None
        # build subapp
        self.__build_widgetbox_left()
        self.__build_widgetbox_right()
        self.__assemble_interface()

    # ---------- widget boxes ---------
    def __build_widgetbox_left(self):
        self.widget['Text_Name'] = wdg.Text(value='', placeholder='John Smith', description='Name')
        self.widget['Text_Email'] = wdg.Text(value='',
                                             placeholder='john.smith@dtu.dk',
                                             description='Email')
        self.widget['Text_Address'] = wdg.Text(value='',
                                               placeholder='Long street 1, 0000 City, Country',
                                               description='Address')
        self.widget_box['left'] = wdg.VBox(
            [self.widget['Text_Name'], self.widget['Text_Email'], self.widget['Text_Address']])

    def __build_widgetbox_right(self):
        self.widget['Text_Partner'] = wdg.Text(value='', placeholder='DTU', description='Partner')
        self.widget['Text_Task'] = wdg.Text(value='',
                                            placeholder='C-rate tests',
                                            description='Task')
        self.widget['Text_Wp'] = wdg.Dropdown(
            options=['WP{}'.format(str(i + 1)) for i in range(11)],
            description='Work package',
            style={'description_width': 'initial'})
        self.widget_box['right'] = wdg.VBox(
            [self.widget['Text_Partner'], self.widget['Text_Task'], self.widget['Text_Wp']])

    # ---------- interface ---------
    def __assemble_interface(self):
        self.widget['Title'] = wdg.HTML(value='<h2>Contact Information</h2>')
        self.interface = wdg.VBox(
            [self.widget['Title'],
             wdg.HBox([self.widget_box['left'], self.widget_box['right']])])

    # ---------- API ---------
    def are_user_inputs_ok(self):
        # returns (ok, error_message)
        ok = True
        error_mesagge = ''
        # check name
        if not self.widget['Text_Name'].value.strip() or self.widget['Text_Name'].value.strip().count(' ') < 1 or \
                self.widget['Text_Name'].value.strip().count(' ') > 3:
            error_mesagge = 'Verify your name is written correctly, e.g.: Name1 Lastname1'
            ok = False
        # check email (simple verification - needs to be improved to discard errors by, for instance, commas, semicolons and other invalid email characters)
        elif not self.widget['Text_Email'].value.strip() or self.widget['Text_Email'].value.strip(
        ).find('@') == -1:
            error_mesagge = 'Verify your email is written correctly, e.g.: username@domain.dk'
            ok = False
        elif not self.widget['Text_Partner'].value:
            error_mesagge = 'Please add the name of the partner institution'
            ok = False
        elif not self.widget['Text_Address'].value:
            error_mesagge = 'Please specify an address'
            ok = False
        elif not self.widget['Text_Task'].value:
            error_mesagge = 'Please briefly describe what the material will be used for'
            ok = False
        return (ok, error_mesagge)

    def get_contact_details(self) -> ContactDetails:
        """Returns a ContactDetails object based on the current values in the form"""
        return ContactDetails(name=self.widget['Text_Name'].value,
                              email=self.widget['Text_Email'].value,
                              institution=self.widget['Text_Partner'].value,
                              address=self.widget['Text_Address'].value,
                              task=self.widget['Text_Task'].value,
                              work_package=self.widget['Text_Wp'].value)


class SelectOrderSubapp:
    """Select order subapp"""

    def __init__(self, form_data_schema):
        # available_materials: dictionary with three (nested) levels: component, category and subcategory
        # -------- subapp attributes
        self.am = form_data_schema
        self.widget = {}
        self.widget_box = {}
        self.interface = None
        # -------- build subapp
        self.__build_widgetbox_selection()
        self.__build_widgetbox_amounts_container()
        self.__assemble_interface()
        self.display_material_info()
        self.render_dynamic_widgetbox_amounts()

    # ---------- widget boxes ---------
    def __build_widgetbox_selection(self):
        self.widget['Toggle_components'] = wdg.ToggleButtons(options=self.am.keys())
        self.widget['Dropdown_category'] = wdg.Dropdown(
            options=self.am[self.widget['Toggle_components'].value].keys(), description='Category')
        self.widget['Dropdown_subcategory'] = wdg.Dropdown(options=self.am[
            self.widget['Toggle_components'].value][self.widget['Dropdown_category'].value].keys(),
                                                           description='Subcategory')
        self.widget_box['selection'] = wdg.VBox([
            self.widget['Toggle_components'], self.widget['Dropdown_category'],
            self.widget['Dropdown_subcategory']
        ])

    def __build_widgetbox_amounts_container(self):
        self.widget['HTML_matinfo'] = wdg.HTML()
        self.widget['Output_amount'] = wdg.Output()
        self.widget_box['amounts'] = wdg.VBox(
            [self.widget['HTML_matinfo'], self.widget['Output_amount']])

    # ---------- interface ---------
    def __assemble_interface(self):
        self.widget['Title'] = wdg.HTML(value='<h2>Select Material</h2>')
        self.interface = wdg.VBox(
            [self.widget['Title'], self.widget_box['selection'], self.widget_box['amounts']])

    # -------- API --------
    def display_material_info(self):
        component, category, subcategory = self.widget['Toggle_components'].value, self.widget[
            'Dropdown_category'].value, self.widget['Dropdown_subcategory'].value
        html_text = '<p><u>{} {}</u> <br>'.format(category, subcategory)
        for key, value in self.am[component][category][subcategory]['properties'].items():
            html_text += key + ': ' + value + '<br>'
        self.widget['HTML_matinfo'].value = html_text + '</p>'

    def render_dynamic_widgetbox_amounts(self):
        component, category, subcategory = self.widget['Toggle_components'].value, self.widget[
            'Dropdown_category'].value, self.widget['Dropdown_subcategory'].value
        self.widget['Output_amount'].clear_output()
        self.widget['Dynamic'] = {}
        for input_key, input_value in self.am[component][category][subcategory]['input'].items():
            if isinstance(input_value, int):
                self.widget['Dynamic'][input_key] = wdg.BoundedIntText(
                    value=input_value,
                    description=input_key,
                    min=0,
                    max=1000,
                    style={'description_width': 'initial'})
            elif isinstance(input_value, str):
                self.widget['Dynamic'][input_key] = wdg.Textarea(
                    description=input_key,
                    value='',
                    placeholder='Describe your request',
                    style={'description_width': 'initial'})
            elif isinstance(input_value, list):
                self.widget['Dynamic'][input_key] = wdg.Dropdown(
                    description=input_key,
                    options=input_value,
                    value=input_value[0],
                    style={'description_width': 'initial'})
        with self.widget['Output_amount']:
            IPython.display.display(wdg.VBox([*self.widget['Dynamic'].values()]))

    def update_category(self):
        self.widget['Dropdown_category'].options = self.am[
            self.widget['Toggle_components'].value].keys()

    def update_subcategory(self):
        self.widget['Dropdown_subcategory'].options = self.am[
            self.widget['Toggle_components'].value][self.widget['Dropdown_category'].value].keys()

    def get_input_fields(self) -> OrderDetails:
        component = self.widget['Toggle_components'].value
        category = self.widget['Dropdown_category'].value
        subcategory = self.widget['Dropdown_subcategory'].value

        order_details = OrderDetails(
            component=component,
            category=category,
            subcategory=subcategory,
            specifications={
                key: value
                for key, value in self.am[component][category][subcategory]['properties'].items()
            },
            amounts={
                key: self.widget['Dynamic'][key].value for key in self.widget['Dynamic'].keys()
            })
        return order_details


class SubmitOrderSubapp:
    """Submit order subapp"""

    def __init__(self, form_data_schema):
        self.am = form_data_schema
        self.widget = {}
        self.widget_box = {}
        self.interface = None
        #
        self.__build_widgetbox_order()
        self.__assemble_interface()

    def __build_widgetbox_order(self):
        self.widget['HTML_error'] = wdg.HTML()
        self.widget['Button_prepare'] = wdg.Button(description='Prepare order', icon='cart-plus')
        self.widget['HTML_review'] = wdg.HTML()
        self.widget['Button_submit'] = wdg.Button(description='Submit order',
                                                  icon='server',
                                                  disabled=True,
                                                  button_style='info')
        self.widget_box = wdg.VBox([
            self.widget['HTML_error'], self.widget['Button_prepare'], self.widget['HTML_review'],
            self.widget['Button_submit']
        ])

    def __assemble_interface(self):
        self.widget['Title'] = wdg.HTML(value='<h2>Review and Submit Order</h2>')
        self.interface = wdg.VBox([
            self.widget['Title'], self.widget['Button_prepare'], self.widget['HTML_error'],
            self.widget['HTML_review'], self.widget['Button_submit']
        ])

    def render_error_message(self, message):
        self.widget['HTML_error'].value = '<p style="color: rgb(255,0,0)">{}<p>'.format(message)

    def clear_error_message(self):
        self.widget['HTML_error'].value = ''

    def render_order_review(self, order: MaterialsOrder):
        self.widget['HTML_review'].value = order.get_html()

    def clear_order_review(self):
        self.widget['HTML_review'].value = ''

    def enable_submission(self):
        self.widget['Button_submit'].disabled = False

    def disable_submission(self):
        self.widget['Button_submit'].disabled = True


class MaterialsAcquisitionForm:
    """The main materials acquisition form app"""

    def __init__(self):
        self.subapp_contact = ContactInfoSubapp()
        self.subapp_selection = SelectOrderSubapp(form_data_schema)
        self.subapp_submission = SubmitOrderSubapp(form_data_schema)
        self.interface = None
        #
        self.__assemble_app()
        self.__widget_events()

    def __assemble_app(self):
        self.interface = wdg.VBox([
            self.subapp_contact.interface, self.subapp_selection.interface,
            self.subapp_submission.interface
        ])

    def __widget_events(self):
        self.subapp_selection.widget['Toggle_components'].observe(self.callback_select_component,
                                                                  names='value')
        self.subapp_selection.widget['Dropdown_category'].observe(self.callback_select_category,
                                                                  names='value')
        self.subapp_selection.widget['Dropdown_subcategory'].observe(
            self.callback_select_subcategory, names='value')
        self.subapp_submission.widget['Button_prepare'].on_click(self.callback_prepare_order)
        self.subapp_submission.widget['Button_submit'].on_click(self.callback_submit_order)

    def callback_select_component(self, _):
        self.subapp_selection.update_category()
        self.subapp_selection.update_subcategory()
        self.subapp_selection.display_material_info()
        self.subapp_selection.render_dynamic_widgetbox_amounts()
        self.subapp_submission.clear_error_message()
        self.subapp_submission.clear_order_review()
        self.subapp_submission.disable_submission()

    def callback_select_category(self, _):
        self.subapp_selection.update_category()
        self.subapp_selection.update_subcategory()
        self.subapp_selection.display_material_info()
        self.subapp_selection.render_dynamic_widgetbox_amounts()
        self.subapp_submission.clear_error_message()
        self.subapp_submission.clear_order_review()
        self.subapp_submission.disable_submission()

    def callback_select_subcategory(self, _):
        self.subapp_selection.display_material_info()
        self.subapp_selection.render_dynamic_widgetbox_amounts()
        self.subapp_submission.clear_error_message()
        self.subapp_submission.clear_order_review()
        self.subapp_submission.disable_submission()

    def callback_prepare_order(self, _):
        ok, error_message = self.subapp_contact.are_user_inputs_ok()
        if ok:
            contact_details = self.subapp_contact.get_contact_details()
            order_details = self.subapp_selection.get_input_fields()
            order = MaterialsOrder(contact_details, order_details)
            self.subapp_submission.render_order_review(order)
            self.subapp_submission.enable_submission()
            self.subapp_submission.clear_error_message()
        else:
            self.subapp_submission.render_error_message(error_message)
            self.subapp_submission.disable_submission()

    def callback_submit_order(self, _):
        contact_details = self.subapp_contact.get_contact_details()
        order_details = self.subapp_selection.get_input_fields()
        order = MaterialsOrder(contact_details, order_details)

        historian = mincepy.connect(
            'mongodb+srv://{USERNAME_HERE}:{PASSWORD_HERE}@cluster0.507lc.mongodb.net/eibar-testing?retryWrites=true&w=majority',
        )
        historian.save(order)
        print('Order saved')


MINCEPY_TYPES = (MaterialsOrder, OrderDetails, ContactDetails)
