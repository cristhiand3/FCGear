#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************


import os
from PySide import QtGui

freecad_found = True

try:
    import FreeCADGui as Gui
    import FreeCAD as App
except ImportError:
    freecad_found = False

if freecad_found:

    import freecad_gear as gear
    from freecad_gear.freecad.commands import (createInvoluteGear,
            createCycloidGear, createBevelGear, createInvoluteRack)



    def add_gear_wb(*args):
        print("Workbench_changed")
        try:
            wb = Gui.activeWorkbench()
        except Exception as e:
            return

        if "PartWorkbench" in str(wb):

            mainWindow = Gui.getMainWindow()

            # add the module to Freecad
            App.gear = gear

            # create toolbar
            App.gear.gear_toolbar = mainWindow.addToolBar("Part: GearToolbar")
            App.gear.gear_toolbar.setObjectName("GearToolbar")

            this_path = os.path.dirname(os.path.realpath(__file__))

            # create commands
            icon = QtGui.QIcon(this_path + "/Resources/icons/involutegear.svg")
            involuteGearAction = QtGui.QAction(icon, "involute gear", App.gear.gear_toolbar)
            involuteGearAction.setObjectName("GearToolbar")
            involuteGearAction.triggered.connect(createInvoluteGear)

            icon = QtGui.QIcon(this_path + "/Resources/icons/involuterack.svg")
            involuteRackAction = QtGui.QAction(icon, "involute rack", App.gear.gear_toolbar)
            involuteRackAction.setObjectName("GearToolbar")
            involuteRackAction.triggered.connect(createInvoluteRack)

            icon = QtGui.QIcon(this_path + "/Resources/icons/cycloidegear.svg")
            cycloidGearAction = QtGui.QAction(icon, "cycloid gear", App.gear.gear_toolbar)
            cycloidGearAction.setObjectName("GearToolbar")
            cycloidGearAction.triggered.connect(createCycloidGear)

            icon = QtGui.QIcon(this_path + "/Resources/icons/bevelgear.svg")
            bevelGearAction = QtGui.QAction(icon, "bevel gear", App.gear.gear_toolbar)
            bevelGearAction.setObjectName("GearToolbar")
            bevelGearAction.triggered.connect(createBevelGear)

            temp1 = App.gear.gear_toolbar.addAction(involuteGearAction)
            temp2 = App.gear.gear_toolbar.addAction(involuteRackAction)
            temp3 = App.gear.gear_toolbar.addAction(cycloidGearAction)
            temp4 = App.gear.gear_toolbar.addAction(bevelGearAction)

    mw = Gui.getMainWindow()
    add_gear_wb()
    mw.workbenchActivated.connect(add_gear_wb)