I-Logix-RPY-Archive version 8.6.0 Java 4012249
{ IProject 
	- _id = GUID 1c12bd3a-bd4c-4d3d-910b-b3992d808cc0;
	- _myState = 8192;
	- _name = "Practica2";
	- _lastID = 3;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 68c07cdf-0a99-4f55-a4f1-a03236f40477;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
		}
		{ IProfile 
			- fileName = "JavaDocProfile";
			- _persistAs = "$OMROOT\\Profiles\\JavaDoc\\";
			- _id = GUID 19700e28-456f-4c97-a19c-b95dcb3e9dff;
			- _isReference = 1;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 203b5c7e-a4c8-41d1-ad2a-fe3c8938ae7f;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Aggregation";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Composition";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "ShowAttributes";
										- _Value = "All";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,None,Public,Explicit";
									}
								}
							}
						}
					}
				}
			}
			- _name = "Modelo Estructural del Dominio";
			- _lastModifiedTime = "12.7.2013::20:38:28";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 76d1aed2-e073-41ca-a7b9-3461f9348bc4;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 203b5c7e-a4c8-41d1-ad2a-fe3c8938ae7f;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 20;
				{ CGIClass 
					- _id = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 5ff2363b-6502-4cbc-a476-94b3af09fa64;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Usuario";
						- _id = GUID 2aee8c37-0a5c-4eaf-ab50-267b7568166d;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Usuario";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.159584 0 0 0.0855614 295.681 396.85 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=76%,24%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Usuario";
							- _name = "QR";
							- _id = GUID ce0be95f-9209-46b0-95d7-9c85137cce5b;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 55e11272-c9ed-4a90-bd3e-82ece6391efa;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Persona";
						- _id = GUID daf2598c-4992-4bae-bea8-66a6e5dcd3ba;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Persona";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.136923 0 0 0.0837791 444.726 217.438 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=81%,19%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Persona";
							- _name = "DNI";
							- _id = GUID 652586e6-eefb-4607-8b5d-7b17fa9aee6c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Persona";
							- _name = "Nombre";
							- _id = GUID 5b63b97b-3f07-4e29-8b30-f7d1ebb8fa9b;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Persona";
							- _name = "Apellidos";
							- _id = GUID ba823751-8f4a-4d21-b7f1-3ccd3a35fb0b;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 0c38dcec-38b7-4ee5-990b-6325e7009448;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Alerta";
						- _id = GUID cb68a83a-577f-4668-b6bb-e93b40309fcd;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Alerta";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.151085 0 0 0.0891266 21.6976 386.677 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=79%,21%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Alerta";
							- _name = "Descripcion";
							- _id = GUID a2a2659e-e3e1-47e6-8450-11aac12559a9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Alerta";
							- _name = "Texto";
							- _id = GUID c4f3c255-14be-42c2-bba3-b165bdc1359d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Alerta";
							- _name = "Fecha";
							- _id = GUID 9bf1c58a-5714-4958-9212-318b6c23ab8e;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID a0c24a49-9322-4cea-852f-379125da4571;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Usuario";
						- _name = "Persona";
						- _id = GUID aa5d2e8b-a6f3-4e3e-a52c-728497e5a2a0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- m_sourceType = 'F';
					- m_pTarget = GUID 55e11272-c9ed-4a90-bd3e-82ece6391efa;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 382 410  514 410  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 541 645 ;
					- m_TargetPort = 506 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 01f51ecf-bf0a-4735-945e-439e950acae7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Sanitario";
						- _name = "Persona";
						- _id = GUID ea92717f-e7aa-447e-befa-20b4617c8c43;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1e288d2d-751f-4984-9cf2-4b13d2b2bf8f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 55e11272-c9ed-4a90-bd3e-82ece6391efa;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 653 410  514 410  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 353 1057 ;
					- m_TargetPort = 506 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID 77af5258-a646-40dd-b8e1-0b63e945ec57;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Evento";
						- _name = "itsUsuario";
						- _id = GUID 93831719-425c-4395-81fc-31273d3ccdc0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3cd28b7d-291c-41ea-99f3-4c914d08ea78;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 702 961 ;
					- m_TargetPort = 710 1358 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Usuario";
						- _name = "itsEvento";
						- _id = GUID 397266e4-dcd4-4f33-a1f2-1958d8b183ab;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID 1da7f8c9-5f16-4def-961f-d55303a86cfc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Recomendacion";
						- _id = GUID 77e2629d-6094-4fac-8488-cdd52ffeafc8;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Recomendacion";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.154863 0 0 0.0962566 686.69 197.332 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=78%,22%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Recomendacion";
							- _name = "Titulo";
							- _id = GUID a99fa804-c75c-41f5-a033-64d52a8c4eaa;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Recomendacion";
							- _name = "Descripcion";
							- _id = GUID 6dc48d57-2212-405a-9831-4f6b55797382;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID be960087-ffa6-4c95-a1a3-19793a4759f7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "PuntoDeInteres";
						- _id = GUID f2712cf3-36a1-4b04-bf21-b02c0c305bb3;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "PuntoDeInteres";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.154863 0 0 0.097148 881.69 192.038 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=79%,21%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "PuntoDeInteres";
							- _name = "Nombre";
							- _id = GUID 5be2d102-dd68-4e45-b317-7a6903d6484e;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "PuntoDeInteres";
							- _name = "Coordenadas";
							- _id = GUID efa02e1d-c683-4451-8fbd-4ac8803cdb4d;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID b04f951b-6a5f-424f-955d-b0540c15c9d5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Enfermedad";
						- _id = GUID 51b89127-b507-4a8a-bad6-4db128091cf1;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Enfermedad";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.151086 0 0 0.0864528 20.6974 275.557 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=79%,21%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Enfermedad";
							- _name = "Nombre";
							- _id = GUID a59d6960-ac04-4c39-b4fd-a2bdef6aaf4c;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 1e288d2d-751f-4984-9cf2-4b13d2b2bf8f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Sanitario";
						- _id = GUID 6a8b69b9-023c-4a97-8bdc-b8783b107bfc;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Sanitario";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.159584 0 0 0.0837789 596.681 393.438 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=83%,17%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Sanitario";
							- _name = "Departamento";
							- _id = GUID 42df02bc-3c6f-4087-8e0e-4ef5b6715683;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 3cd28b7d-291c-41ea-99f3-4c914d08ea78;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Evento";
						- _id = GUID c8021acb-09e9-4a92-9c6c-c21cd9a7e909;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Evento";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.15864 0 0 0.112299 297.683 576.055 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=84%,16%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Evento";
							- _name = "Nombre";
							- _id = GUID cf3f9037-b388-4233-a60a-5fc2edb1a113;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Evento";
							- _name = "Fecha";
							- _id = GUID f1534706-ad87-49c6-9db4-8dab1544b4f6;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Evento";
							- _name = "Hora";
							- _id = GUID e372074d-817a-4e66-8a6e-9e9e81e2f718;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Evento";
							- _name = "Tipo";
							- _id = GUID a83230dc-02fc-4220-a768-023a27139339;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID ebb5b4dd-3c8b-4118-acb0-f14f8cf87af1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Cita";
						- _id = GUID 0839d6f6-285f-4dd3-bbda-d1c97f1d607f;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Cita";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.151086 0 0 0.0989305 606.698 599.452 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=77%,23%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Cita";
							- _name = "Consulta";
							- _id = GUID 784a7514-783b-487c-b848-98725c370a95;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 75d68696-c749-4c23-8f9c-778cb2cf4f49;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Cita";
						- _name = "Evento";
						- _id = GUID d7cb9b62-a4b2-4ae3-88b9-5618967f8909;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ebb5b4dd-3c8b-4118-acb0-f14f8cf87af1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3cd28b7d-291c-41ea-99f3-4c914d08ea78;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 2 875 ;
					- m_TargetPort = 1042 979 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID a4782ced-784e-48b8-af1c-3a4408c83838;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Cita";
						- _name = "itsSanitario";
						- _id = GUID 9835d505-5a16-4cf6-a071-662f455416d3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ebb5b4dd-3c8b-4118-acb0-f14f8cf87af1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1e288d2d-751f-4984-9cf2-4b13d2b2bf8f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 525 905 ;
					- m_TargetPort = 560 914 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Sanitario";
						- _name = "itsCita";
						- _id = GUID e9af4876-9001-4fdc-a73a-204845d80c8b;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 9ac15f66-c370-4bf1-ace8-0661fcf4a2e8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Usuario";
						- _name = "itsEnfermedad_2";
						- _id = GUID 46d00e12-4303-4016-8326-14dea8cf6007;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- m_sourceType = 'F';
					- m_pTarget = GUID b04f951b-6a5f-424f-955d-b0540c15c9d5;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 241 463  241 399  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 340 773 ;
					- m_TargetPort = 796 1428 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Enfermedad";
						- _name = "itsUsuario_1";
						- _id = GUID eb93be30-1a21-4a42-9db7-7d3d3ff06f51;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 6390918f-900b-49bc-b449-e4723a9f4d8f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Usuario";
						- _name = "itsAlerta_2";
						- _id = GUID 03056d49-5ab2-4a2f-817e-a58dc3b69d97;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0c38dcec-38b7-4ee5-990b-6325e7009448;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 241 483  241 491  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 83 1007 ;
					- m_TargetPort = 909 1171 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Alerta";
						- _name = "itsUsuario";
						- _id = GUID d28d4382-869d-48ce-83ad-d7cf8c0000e9;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID 8498911b-b05c-4f59-abc4-2fcdb44b37da;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "BDU";
						- _id = GUID 6332044c-8c36-47fc-a67b-5d9d56d09b8b;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "BDU";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.115203 0 0 0.0828875 900.769 344.73 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 2215e88e-da60-4ce3-99bc-86652f1b4cb2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Conexion";
						- _id = GUID 28533111-b57e-4d8a-ab2c-1391bdf54d04;
					}
					- m_pParent = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
					- m_name = { CGIText 
						- m_str = "Conexion";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.152974 0 0 0.0864528 16.6941 502.557 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=72%,28%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Conexion";
							- _name = "Fecha";
							- _id = GUID 43729524-b360-46c4-946c-6591be4c51f4;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Conexion";
							- _name = "Coordenadas";
							- _id = GUID 74c3be35-ee86-4bfd-a76e-ed03bce21ba0;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 677f2986-4338-4085-b071-32715d554fb2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Conexion";
						- _name = "itsUsuario";
						- _id = GUID 241cc4d5-2142-4154-a0a6-20e53e48f76a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2215e88e-da60-4ce3-99bc-86652f1b4cb2;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4e8f2179-8371-4ff2-82bf-ab3daa886396;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 237 567  237 511  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1054 745 ;
					- m_TargetPort = 8 1334 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Usuario";
						- _name = "itsConexion";
						- _id = GUID 49d5b1a9-d3fd-4dcd-bb25-13e4af81696b;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "0..*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 4040e9be-1621-4470-9dfb-cf3d7a349873;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
		}
	}
	- MSCS = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMSC 
			- _id = GUID 53ecd8fb-251b-403b-a0b0-77b59cc404a0;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 11;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "DestructionEvent";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,30,30";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "2";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "EnvironmentLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOccurrence";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,134";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Note";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "250,244,212";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PartitionLine";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,300,0";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "AutoCreateExecutionOccurrence";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ShowSequenceNumbers";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Caso de uso 1.1";
			- _lastModifiedTime = "12.5.2013::12:45:8";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 654575e8-30e9-4c04-8d7d-5d743633f0d5;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 53ecd8fb-251b-403b-a0b0-77b59cc404a0;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 40;
				{ CGIBox 
					- _id = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID a274fbc2-9d1a-49fc-84ba-08164fd9e69d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 6059c48c-59b1-4d80-b3f4-3fee2a26fe64;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 04eab446-41da-4ddc-ae04-d1486332e8fb;
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 100 313  525 313  525 743  100 743  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=267,163>
<frame Id=GUID 678fc654-f461-4b29-b92e-1235100e449a>
<frame Id=GUID a8a5e086-0cb7-4bce-b56c-4d9721c61096>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID c107b838-8722-4d61-8e06-302b76254895;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 0398dbc2-1a69-4a2a-aceb-1c48ca3fcdf5;
					}
					- m_pParent = GUID 5ad38ab7-96a7-47dd-88ba-7771ca8855e6;
					- m_name = { CGIText 
						- m_str = "else";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 113 1060  496 1060  496 1147  113 1147  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 6eb69110-abca-4458-915b-43019010a4c1;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 97de05cd-5ffd-476d-840d-317920d3620d;
					}
					- m_pParent = GUID 5ad38ab7-96a7-47dd-88ba-7771ca8855e6;
					- m_name = { CGIText 
						- m_str = "cancelar";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 113 982  496 982  496 1060  113 1060  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID a8a5e086-0cb7-4bce-b56c-4d9721c61096;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID a5ee702c-b6c4-47db-9328-6c65c8c4a00d;
					}
					- m_pParent = GUID 6059c48c-59b1-4d80-b3f4-3fee2a26fe64;
					- m_name = { CGIText 
						- m_str = "else";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 100 580  525 580  525 743  100 743  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 678fc654-f461-4b29-b92e-1235100e449a;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 5842ac61-f407-4821-ad7a-b50d384935af;
					}
					- m_pParent = GUID 6059c48c-59b1-4d80-b3f4-3fee2a26fe64;
					- m_name = { CGIText 
						- m_str = "if(registrado en BDU)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 100 313  525 313  525 580  100 580  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 1901e848-df18-4453-b838-34bc4cc1738b;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 04ebc60c-e2e9-47b9-8e6d-89386421391d;
					}
					- m_pParent = GUID de2785e4-1475-4511-b814-63cb9b23c027;
					- m_name = { CGIText 
						- m_str = "else";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 131 515  487 515  487 594  131 594  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID a643ca0e-e345-414e-8f3e-2fe9e6d6ba20;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 15a2b38b-a775-430d-b16d-83f84a31058c;
					}
					- m_pParent = GUID de2785e4-1475-4511-b814-63cb9b23c027;
					- m_name = { CGIText 
						- m_str = "cancelar";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 131 435  487 435  487 515  131 515  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID de2785e4-1475-4511-b814-63cb9b23c027;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID a3787875-9b3b-4ce0-9ffc-526e56aff77c;
					}
					- m_pParent = GUID 678fc654-f461-4b29-b92e-1235100e449a;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.05618 0 0 1 -21.3596 -23 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 131 435  487 435  487 594  131 594  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=80,79>
<frame Id=GUID a643ca0e-e345-414e-8f3e-2fe9e6d6ba20>
<frame Id=GUID 1901e848-df18-4453-b838-34bc4cc1738b>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 5ad38ab7-96a7-47dd-88ba-7771ca8855e6;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 9062c062-c167-4054-8567-54741bb3c507;
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "interactionOperator_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 -76 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 113 982  496 982  496 1147  113 1147  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=78,87>
<frame Id=GUID 6eb69110-abca-4458-915b-43019010a4c1>
<frame Id=GUID c107b838-8722-4d61-8e06-302b76254895>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = ":Sanitario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.02438 94 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 447ec8fd-d2d8-478b-a5bd-a6c5b51e6756;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 7fe922f8-8e0b-4cde-958d-eba2e41d8b84;
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = ":BDU";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0244362 430 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_type = 118;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "ENV";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.02438 247 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9659ee83-8e69-4aef-8593-905a67f6047a;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 683146db-da27-43e6-a360-db009b252363;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 41.0172 42 5127.17 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID dabf6e4b-0139-40d7-b4e6-19acab77241d;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 5215d50a-7135-49dd-9d76-ad702267e6db;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID af7928aa-3bf9-4ce2-8e5c-2b3a8839a65e;
					}
					- m_pParent = GUID 447ec8fd-d2d8-478b-a5bd-a6c5b51e6756;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 47.7434 42 7816.26 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID ef62ae89-8435-44b9-a6a5-6477ccd39164;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID fdb42371-dccf-466d-bf70-4b8eb18e9bf5;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c9cb6d66-4516-41e6-9011-7b5a1951e204;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 41.0172 42 22969.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID bb6780a0-241f-469d-b848-5d9ff7be7dcd;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID f0e31e83-ae58-4d6f-af36-e6da7fed1df8;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 43d4afae-f962-40e0-81ba-95f1664d6cae;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 48.9928 42 12346.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID a38592c3-3e95-45ed-92f4-5ee969c8fcb0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 2f0eabf6-1d48-4740-a03f-00fe00a13668;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c85680d5-c3fe-4b9c-bd59-ee1b647a438b;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 55.829 42 31214.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID ed48a9bc-8c75-4f90-b63f-283eeba7afe9;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID bfec98be-d2d0-4a76-8a2b-e0c09457fda6;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 483cf5e9-878f-4774-aae9-4a18066d1fe7;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 41.0172 42 39458.6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 06ccea35-f5a2-412a-889c-22eaa831139b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID c515e518-e026-4795-96bc-81bdca5555c4;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID afd176c1-07d9-46f3-90ec-fccf50335042;
					}
					- m_pParent = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 41.0172 42 19401.2 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID d66c0984-9596-4ad2-838a-583d668ce9fb;
				}
				{ CGIMscColumnCR 
					- _id = GUID aaefc0aa-b247-45bb-b4a9-ea15ca24d550;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 224 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 693f25a0-52b8-402c-9771-13adb518a95a;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 5";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 777 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID b769b8c3-05ef-4a7d-bf35-d6ab71ede524;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 7";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 1100 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID a2737c86-089d-412f-9971-7becd69195f2;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 333 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 424fa846-b9d4-4683-901b-6637de386870;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 153 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 366018f8-1ddc-4211-8000-70fece94cdec;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 405 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 5d54c726-0fcb-4911-9872-6405b7e3c869;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
					- m_name = { CGIText 
						- m_str = "Punto 6";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.28 0 0 1 0 892 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscMessage 
					- _id = GUID ef62ae89-8435-44b9-a6a5-6477ccd39164;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID bd2e8563-fe1c-4d0e-b3bf-96d0343f7955;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "comprobarRegistro()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_sourceType = 'F';
					- m_pTarget = GUID 447ec8fd-d2d8-478b-a5bd-a6c5b51e6756;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 7834 ;
					- m_TargetPort = 48 7816 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID 5215d50a-7135-49dd-9d76-ad702267e6db;
				}
				{ CGIMscMessage 
					- _id = GUID 06ccea35-f5a2-412a-889c-22eaa831139b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d84c4413-7b91-4fc7-843d-8df4511d3081;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "confirmarRasgosSanitarios()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  143 -9  143 5  -6 5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 150 919 ;
						- m_nHorizontalSpacing = -4;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 39459 ;
					- m_TargetPort = 48 39459 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID bfec98be-d2d0-4a76-8a2b-e0c09457fda6;
				}
				{ CGIMscMessage 
					- _id = GUID dabf6e4b-0139-40d7-b4e6-19acab77241d;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 593e6466-9773-4b98-94ae-bc429964f252;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "indicarNUHSA()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 5127 ;
					- m_TargetPort = 48 5127 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 9659ee83-8e69-4aef-8593-905a67f6047a;
				}
				{ CGIMscMessage 
					- _id = GUID 104ad0f2-9a6b-43cd-97b1-9be1de0f95ff;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a6a725a8-6e56-4e76-817e-20e2e2694963;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "generarBoletin()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_sourceType = 'F';
					- m_pTarget = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 45078 ;
					- m_TargetPort = 48 45078 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID d66c0984-9596-4ad2-838a-583d668ce9fb;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4345b3f3-a17a-4e05-8980-f5e89afed513;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "confirmarDatos()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 19401 ;
					- m_TargetPort = 48 19401 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID c515e518-e026-4795-96bc-81bdca5555c4;
				}
				{ CGIMscMessage 
					- _id = GUID 051b89ad-6518-481b-ad1c-75d2d8bbfc75;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 215b1ee6-106f-4206-90fa-9daa6e95206e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "reply_comprobarRegistro()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -65 -6  78 -6  78 8  -65 8  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 391 278 ;
						- m_nHorizontalSpacing = -3;
						- m_nVerticalSpacing = 16;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 447ec8fd-d2d8-478b-a5bd-a6c5b51e6756;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 9003 ;
					- m_TargetPort = 48 9024 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID bb6780a0-241f-469d-b848-5d9ff7be7dcd;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3e0ce326-9a30-4dd6-8832-6d120b708a02;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "informarUsuarioSinRegistro()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_sourceType = 'F';
					- m_pTarget = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 22970 ;
					- m_TargetPort = 48 22970 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID fdb42371-dccf-466d-bf70-4b8eb18e9bf5;
				}
				{ CGIMscMessage 
					- _id = GUID ed48a9bc-8c75-4f90-b63f-283eeba7afe9;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 52509e52-712b-4faf-aeee-0106dc58ede5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "indicarRasgosSanitarios()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 31214 ;
					- m_TargetPort = 48 31214 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 2f0eabf6-1d48-4740-a03f-00fe00a13668;
				}
				{ CGIMscMessage 
					- _id = GUID a38592c3-3e95-45ed-92f4-5ee969c8fcb0;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d3d91085-328c-4595-9406-70ae2f7ea792;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mostrarDatosUsuario()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_sourceType = 'F';
					- m_pTarget = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 12346 ;
					- m_TargetPort = 48 12346 ;
					- m_bLeft = 0;
					- m_pTargetExec = GUID f0e31e83-ae58-4d6f-af36-e6da7fed1df8;
				}
				{ CGIMscMessage 
					- _id = GUID f9b6100a-f29f-4011-8790-3605060e32ff;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e170c700-9781-43c9-9f52-67d4b9b9ceac;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mostrarRasgosSanitarios()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8b3d4f0d-a130-4faa-ae40-608cf78f5749;
					- m_sourceType = 'F';
					- m_pTarget = GUID 57547767-becf-492a-8060-71bba42e1c32;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 32404 ;
					- m_TargetPort = 48 32404 ;
					- m_bLeft = 0;
				}
				{ CGIAnnotation 
					- _id = GUID c438e5d7-dad2-4570-af5c-14d110378267;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID a8a5e086-0cb7-4bce-b56c-4d9721c61096;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.328413 0 0 0.0456204 123 651.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 0e7eb0d1-e1fd-4e65-8c26-b96ef51aeb4b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID a643ca0e-e345-414e-8f3e-2fe9e6d6ba20;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.308324 0 0 0.0456204 146.146 456.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 796698ce-21bd-488b-959e-d6524ae1e330;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 6eb69110-abca-4458-915b-43019010a4c1;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.328413 0 0 0.0456204 130 1005.86 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 6e824de2-f3e7-4539-9e6e-557854e108ff;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID a274fbc2-9d1a-49fc-84ba-08164fd9e69d;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IClassifierRole 
						- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						- _myState = 2048;
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Sanitario_actor";
							- _id = GUID 502f7af0-36be-4f67-92ed-c9b218374571;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 7fe922f8-8e0b-4cde-958d-eba2e41d8b84;
						- _myState = 2048;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "BDU";
							- _id = GUID 6332044c-8c36-47fc-a67b-5d9d56d09b8b;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						- _name = "ENV";
						- m_eRoleType = SYSTEM_BORDER;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 10;
					- value = 
					{ IMessage 
						- _id = GUID 593e6466-9773-4b98-94ae-bc429964f252;
						- _name = "indicarNUHSA";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 683146db-da27-43e6-a360-db009b252363;
						}
					}
					{ IMessage 
						- _id = GUID bd2e8563-fe1c-4d0e-b3bf-96d0343f7955;
						- _name = "comprobarRegistro";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7fe922f8-8e0b-4cde-958d-eba2e41d8b84;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "BDU";
							- _name = "comprobarRegistro()";
							- _id = GUID 1be4e248-6873-4416-a3ac-3ec1671f5490;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID af7928aa-3bf9-4ce2-8e5c-2b3a8839a65e;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 215b1ee6-106f-4206-90fa-9daa6e95206e;
						- _name = "reply_comprobarRegistro";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7fe922f8-8e0b-4cde-958d-eba2e41d8b84;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "BDU";
							- _name = "reply_comprobarRegistro()";
							- _id = GUID 328bff43-9cb1-44b2-9bdd-97d3c21ec608;
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3e0ce326-9a30-4dd6-8832-6d120b708a02;
						- _name = "informarUsuarioSinRegistro";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Sanitario_actor";
							- _name = "informarUsuarioSinRegistro()";
							- _id = GUID 5dc36414-ffa1-49b4-b697-ef8948813f78;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c9cb6d66-4516-41e6-9011-7b5a1951e204;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d3d91085-328c-4595-9406-70ae2f7ea792;
						- _name = "mostrarDatosUsuario";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Sanitario_actor";
							- _name = "mostrarDatosUsuario()";
							- _id = GUID 12bb0c78-3d45-4c55-be9b-bb383a436b05;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 43d4afae-f962-40e0-81ba-95f1664d6cae;
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 52509e52-712b-4faf-aeee-0106dc58ede5;
						- _name = "indicarRasgosSanitarios";
						- m_szSequence = "7.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c85680d5-c3fe-4b9c-bd59-ee1b647a438b;
						}
					}
					{ IMessage 
						- _id = GUID d84c4413-7b91-4fc7-843d-8df4511d3081;
						- _name = "confirmarRasgosSanitarios";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 483cf5e9-878f-4774-aae9-4a18066d1fe7;
						}
					}
					{ IMessage 
						- _id = GUID a6a725a8-6e56-4e76-817e-20e2e2694963;
						- _name = "generarBoletin";
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Sanitario_actor";
							- _name = "generarBoletin()";
							- _id = GUID 22285538-b5e3-41b1-af71-94ed6ab211f5;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4345b3f3-a17a-4e05-8980-f5e89afed513;
						- _name = "confirmarDatos";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID afd176c1-07d9-46f3-90ec-fccf50335042;
						}
					}
					{ IMessage 
						- _id = GUID e170c700-9781-43c9-9f52-67d4b9b9ceac;
						- _name = "mostrarRasgosSanitarios";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d23bb230-747f-4d3d-b8cf-d3b7865fff50;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6a2a99b4-fcbe-40fd-947a-442f8e66e903;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 7;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID 683146db-da27-43e6-a360-db009b252363;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 593e6466-9773-4b98-94ae-bc429964f252;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID af7928aa-3bf9-4ce2-8e5c-2b3a8839a65e;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID bd2e8563-fe1c-4d0e-b3bf-96d0343f7955;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 42;
					}
					{ IExecutionOccurrence 
						- _id = GUID c9cb6d66-4516-41e6-9011-7b5a1951e204;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 3e0ce326-9a30-4dd6-8832-6d120b708a02;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID 43d4afae-f962-40e0-81ba-95f1664d6cae;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d3d91085-328c-4595-9406-70ae2f7ea792;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 43;
					}
					{ IExecutionOccurrence 
						- _id = GUID c85680d5-c3fe-4b9c-bd59-ee1b647a438b;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 52509e52-712b-4faf-aeee-0106dc58ede5;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 49;
					}
					{ IExecutionOccurrence 
						- _id = GUID 483cf5e9-878f-4774-aae9-4a18066d1fe7;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID d84c4413-7b91-4fc7-843d-8df4511d3081;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
					{ IExecutionOccurrence 
						- _id = GUID afd176c1-07d9-46f3-90ec-fccf50335042;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 4345b3f3-a17a-4e05-8980-f5e89afed513;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 36;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 04eab446-41da-4ddc-ae04-d1486332e8fb;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 5842ac61-f407-4821-ad7a-b50d384935af;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- CombinedFragments = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ ICombinedFragment 
										- _id = GUID a3787875-9b3b-4ce0-9ffc-526e56aff77c;
										- _myState = 2048;
										- _name = "interactionOperator_1";
										- _interactionOperator = "alt";
										- InteractionOperands = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IInteractionOperand 
												- _id = GUID 15a2b38b-a775-430d-b16d-83f84a31058c;
												- _myState = 2048;
												- _name = "interactionOperand_0";
												- _interactionConstraint = "cancelar";
											}
											{ IInteractionOperand 
												- _id = GUID 04ebc60c-e2e9-47b9-8e6d-89386421391d;
												- _myState = 2048;
												- _name = "interactionOperand_1";
												- _interactionConstraint = "else";
											}
										}
									}
								}
								- _interactionConstraint = "if(registrado en BDU)";
							}
							{ IInteractionOperand 
								- _id = GUID a5ee702c-b6c4-47db-9328-6c65c8c4a00d;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _interactionConstraint = "else";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 9062c062-c167-4054-8567-54741bb3c507;
						- _myState = 2048;
						- _name = "interactionOperator_2";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 97de05cd-5ffd-476d-840d-317920d3620d;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "cancelar";
							}
							{ IInteractionOperand 
								- _id = GUID 0398dbc2-1a69-4a2a-aceb-1c48ca3fcdf5;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _interactionConstraint = "else";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID d303741a-5c49-4399-b9b9-83dbf0dcfbfe;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "EnvironmentLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOccurrence";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,134";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Note";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "250,244,212";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PartitionLine";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,300,0";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "AutoCreateExecutionOccurrence";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Caso de uso 1.2";
			- _lastModifiedTime = "12.5.2013::12:27:15";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 4c34bc42-3135-473e-96d2-1019fa08b1f0;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID d303741a-5c49-4399-b9b9-83dbf0dcfbfe;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 36;
				{ CGIBox 
					- _id = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 472577d1-1a77-4539-8e58-f65f23481ccd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID a86aa714-49b3-4396-86c1-8a059d65c0e1;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 1639cb7b-8b1e-4593-ac99-1b12c91d69cc;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 -9 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 118 188  551 188  551 342  118 342  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=61,93>
<frame Id=GUID f4dca511-66d6-4de0-9a01-6011c2a9fd2f>
<frame Id=GUID 500912d3-7af8-4de2-a230-a65aeb52a2e6>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 510ee27d-b570-4661-bd80-f5bbd57e16b2;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 6cc5b213-aca8-4893-bd05-90376b6a352f;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 118 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 147 354  519 354  519 462  147 462  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=108>
<frame Id=GUID fe54803b-905a-4b5a-b6e2-ddff5301a9bf>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID a62a01c3-7067-4faf-8620-40aa4ddbed54;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 9100f221-8acd-40f1-ab4a-934363fbf981;
					}
					- m_pParent = GUID 5c9e7850-004f-40f5-95ff-a369da3cd577;
					- m_name = { CGIText 
						- m_str = "cancelar";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 146 925  445 925  445 1067  146 1067  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID b8a84805-6b50-4d5f-8d20-036762b9532f;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 80a39ab8-0ed7-4b6a-bcc7-d26dcb89866b;
					}
					- m_pParent = GUID 5c9e7850-004f-40f5-95ff-a369da3cd577;
					- m_name = { CGIText 
						- m_str = "revisar";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 146 815  445 815  445 925  146 925  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 518e6e5f-710a-47a5-90bf-df6accf3cd74;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID e53c2307-45e5-47de-b1a7-c499cbb962a5;
					}
					- m_pParent = GUID 3a080aa1-ae0e-43e4-9962-f829d887f8ac;
					- m_name = { CGIText 
						- m_str = "primera vez";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 132 737  468 737  468 1166  132 1166  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 500912d3-7af8-4de2-a230-a65aeb52a2e6;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID eed05f27-c85d-4941-a8c2-8f414a52916b;
					}
					- m_pParent = GUID a86aa714-49b3-4396-86c1-8a059d65c0e1;
					- m_name = { CGIText 
						- m_str = "else (ID y Pass)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 118 249  551 249  551 342  118 342  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID f4dca511-66d6-4de0-9a01-6011c2a9fd2f;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 13469516-2e36-473b-813d-d789cc272db6;
					}
					- m_pParent = GUID a86aa714-49b3-4396-86c1-8a059d65c0e1;
					- m_name = { CGIText 
						- m_str = "QR";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 118 188  551 188  551 249  118 249  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID fe54803b-905a-4b5a-b6e2-ddff5301a9bf;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID ffdf39d6-9e9c-4b1d-a3de-69cbd7dfcf9f;
					}
					- m_pParent = GUID 510ee27d-b570-4661-bd80-f5bbd57e16b2;
					- m_name = { CGIText 
						- m_str = "QR erroneo o Sin alta";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 147 354  519 354  519 462  147 462  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 3a080aa1-ae0e-43e4-9962-f829d887f8ac;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 777aa309-0085-4822-9252-ad7925f2b366;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "interactionOperator_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 -3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 132 737  468 737  468 1166  132 1166  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=429>
<frame Id=GUID 518e6e5f-710a-47a5-90bf-df6accf3cd74>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 5c9e7850-004f-40f5-95ff-a369da3cd577;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID ba74f05c-11d1-45bd-82c4-ef23e7b8e575;
					}
					- m_pParent = GUID 518e6e5f-710a-47a5-90bf-df6accf3cd74;
					- m_name = { CGIText 
						- m_str = "interactionOperator_3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 0 -39 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 146 815  445 815  445 1067  146 1067  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=110,142>
<frame Id=GUID b8a84805-6b50-4d5f-8d20-036762b9532f>
<frame Id=GUID a62a01c3-7067-4faf-8620-40aa4ddbed54>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = ":Usuario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.02642 116 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_type = 118;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "ENV";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.02642 358 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 9b76b613-f889-4689-8a21-cee7877f3e5e;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID c74b0fb8-3d66-4efc-b552-d86a7d74cb97;
					}
					- m_pParent = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 64.1348 42 39137.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 77fe7682-4bd3-4856-81ad-ecf9d390ecba;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 3acdedc5-be10-401e-9b2d-c4e1ca590519;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID 2223be72-5cc7-40d2-8f5d-c8aea031a70a;
					}
					- m_pParent = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 51.5182 42 29220.3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 3137e415-08dc-4392-bcf7-ac0aba14f72b;
				}
				{ CGIMscExecutionOccurrence 
					- _id = GUID 82ff49e5-adca-492c-9842-1eae7924486e;
					- m_type = 162;
					- m_pModelObject = { IHandle 
						- _m2Class = "IExecutionOccurrence";
						- _id = GUID d6da81c3-da59-483d-9cc2-74c0edf927bf;
					}
					- m_pParent = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 51.5182 42 33043.1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 4 0 0  0 36  12 36  12 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
					- m_pStartMessage = GUID 3c315e3d-f7db-4e43-ae7b-52cebb8619e6;
				}
				{ CGIMscInteractionOccurrence 
					- _id = GUID 0a8e3e77-50a8-46d7-9f91-883f2815c051;
					- m_type = 172;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOccurrence";
						- _id = GUID 6805d003-970a-45b5-88a8-e386c87f98b3;
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Caso de uso 2.1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.30556 0 0 0.454545 148 1211 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 132  216 132  216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 46ce0dfb-6316-490e-9256-6296036b47c5;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 763 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID e4781142-6422-4abe-8c88-42f040317f32;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 1062 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 2432606d-c224-4627-a218-508c52b97259;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 2b y 5";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 1182 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 8dbb5ac6-0b14-4bfd-9c09-0253c48a1952;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 2a";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 353 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 92800a62-4919-4c41-ae70-b733d0eea596;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 1 alt";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 263 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4064bbd5-fb05-4724-a6cd-ef8d27d2120d;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
					- m_name = { CGIText 
						- m_str = "Punto 1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 2.04 0 0 1 0 199 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscMessage 
					- _id = GUID db2673a8-5bc2-4269-b5c9-b7f65916f964;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 397fd8af-20bf-4da7-9597-db627ff0de19;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "indicarIDyPass()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 8970 ;
					- m_TargetPort = 48 8970 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID d24ca9d0-6daf-46e4-9a86-f4c65cf46623;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c7246513-b525-42c4-bad0-dfadf834d819;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "confirmarActivacionCuenta()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 40689 ;
					- m_TargetPort = 48 40689 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f76fa5bd-e234-48cf-a1b9-1ebdb7f485bb;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3cd2082a-1ed0-4fd3-9261-9904d7667563;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "comprobarAlta()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 435 392  435 451  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 12945 ;
					- m_TargetPort = 48 15178 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID eb35b20b-dcc8-48e4-9161-63a575aec366;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 55735040-58a8-4f44-96d9-0145afb1112f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "comunicarError()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 17260 ;
					- m_TargetPort = 48 17260 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c059d464-708f-4fb2-9f25-84c36fdc7afb;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9b010882-23f2-41e7-bea1-026390312a8f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "capturarQR()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 6435 ;
					- m_TargetPort = 48 6435 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 3c315e3d-f7db-4e43-ae7b-52cebb8619e6;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8f22f481-d935-49c3-b8f8-d89499e234a2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "cancelarDatos()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 33043 ;
					- m_TargetPort = 48 33043 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 82ff49e5-adca-492c-9842-1eae7924486e;
				}
				{ CGIMscMessage 
					- _id = GUID 77fe7682-4bd3-4856-81ad-ecf9d390ecba;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 0a84a3b3-76d2-4378-8068-9a170b6cf3c8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "configurarPerfil()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 39137 ;
					- m_TargetPort = 48 39137 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 9b76b613-f889-4689-8a21-cee7877f3e5e;
				}
				{ CGIMscMessage 
					- _id = GUID 3137e415-08dc-4392-bcf7-ac0aba14f72b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5cae047a-0581-43db-8209-e28bb91f8c35;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "revisarDatosContacto()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_sourceType = 'F';
					- m_pTarget = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 29220 ;
					- m_TargetPort = 48 29220 ;
					- m_bLeft = 0;
					- m_pSourceExec = GUID 3acdedc5-be10-401e-9b2d-c4e1ca590519;
				}
				{ CGIMscMessage 
					- _id = GUID 62e6a239-f0be-449b-b997-fecffc5eebc1;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID fbbf548d-f9f1-4943-af41-f7fcf9683165;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mostrarDatos()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 30318 ;
					- m_TargetPort = 48 30318 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 107f2dc5-c13c-4a9a-9d75-200fc50ff734;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 8f9f68e6-bac2-4b93-861c-66d973953c17;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "cancela()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 34141 ;
					- m_TargetPort = 48 34141 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 34ed47f0-ef25-4c7b-802a-a86e22145419;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 08b55e73-701d-408e-8680-b74c2b673dc8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "mostrarConfiguracion()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 37a499dc-03e3-4426-926c-3c74ec354195;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4c3d2054-3245-47cf-b728-6c03e7d84bcc;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 39932 ;
					- m_TargetPort = 48 39932 ;
					- m_bLeft = 0;
				}
				{ CGIAnnotation 
					- _id = GUID cd7a0095-25d9-481d-b91a-262a4adad37f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 510ee27d-b570-4661-bd80-f5bbd57e16b2;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.328413 0 0 0.0456204 153 401.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 6932821c-917e-4bbc-a793-90193136aa9d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID a62a01c3-7067-4faf-8620-40aa4ddbed54;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.159594 0 0 0.0456204 196 1010.86 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID eb56e479-0de7-4c45-ba0e-99af795ad1f9;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 472577d1-1a77-4539-8e58-f65f23481ccd;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						- _myState = 2048;
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Usuario_actor";
							- _id = GUID c41badc4-79ca-41cb-a7c8-635e31f13532;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						- _name = "ENV";
						- m_eRoleType = SYSTEM_BORDER;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 11;
					- value = 
					{ IMessage 
						- _id = GUID 9b010882-23f2-41e7-bea1-026390312a8f;
						- _name = "capturarQR";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 397fd8af-20bf-4da7-9597-db627ff0de19;
						- _name = "indicarIDyPass";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3cd2082a-1ed0-4fd3-9261-9904d7667563;
						- _name = "comprobarAlta";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 55735040-58a8-4f44-96d9-0145afb1112f;
						- _name = "comunicarError";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Usuario_actor";
							- _name = "comunicarError()";
							- _id = GUID dcd74ec6-7f5a-4d9f-b265-e0e94efe0a86;
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5cae047a-0581-43db-8209-e28bb91f8c35;
						- _name = "revisarDatosContacto";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID 2223be72-5cc7-40d2-8f5d-c8aea031a70a;
						}
					}
					{ IMessage 
						- _id = GUID 0a84a3b3-76d2-4378-8068-9a170b6cf3c8;
						- _name = "configurarPerfil";
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID c74b0fb8-3d66-4efc-b552-d86a7d74cb97;
						}
					}
					{ IMessage 
						- _id = GUID c7246513-b525-42c4-bad0-dfadf834d819;
						- _name = "confirmarActivacionCuenta";
						- m_szSequence = "11.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 8f22f481-d935-49c3-b8f8-d89499e234a2;
						- _name = "cancelarDatos";
						- m_szSequence = "7.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "IExecutionOccurrence";
							- _id = GUID d6da81c3-da59-483d-9cc2-74c0edf927bf;
						}
					}
					{ IMessage 
						- _id = GUID fbbf548d-f9f1-4943-af41-f7fcf9683165;
						- _name = "mostrarDatos";
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 8f9f68e6-bac2-4b93-861c-66d973953c17;
						- _name = "cancela";
						- m_szSequence = "8.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 08b55e73-701d-408e-8680-b74c2b673dc8;
						- _name = "mostrarConfiguracion";
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 030b6249-c06d-4806-ab88-6f3706d6e8fb;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 9cae1d83-8f2a-488c-a940-ec5525bd3897;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- InteractionOccurrences = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IInteractionOccurrence 
						- _id = GUID 6805d003-970a-45b5-88a8-e386c87f98b3;
						- _name = "Caso de uso 2.1";
						- m_pRefSD = { IHandle 
							- _m2Class = "IMSC";
							- _id = GUID 9594ddac-a270-4e9f-89e7-8dfdaf8c96c1;
						}
					}
				}
				- ExecutionOccurrences = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IExecutionOccurrence 
						- _id = GUID c74b0fb8-3d66-4efc-b552-d86a7d74cb97;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 0a84a3b3-76d2-4378-8068-9a170b6cf3c8;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 61;
					}
					{ IExecutionOccurrence 
						- _id = GUID 2223be72-5cc7-40d2-8f5d-c8aea031a70a;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 5cae047a-0581-43db-8209-e28bb91f8c35;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 49;
					}
					{ IExecutionOccurrence 
						- _id = GUID d6da81c3-da59-483d-9cc2-74c0edf927bf;
						- _myState = 2048;
						- _name = "executionoccurrence_0";
						- m_startMessage = { IHandle 
							- _m2Class = "IMessage";
							- _id = GUID 8f22f481-d935-49c3-b8f8-d89499e234a2;
						}
						- m_endMessage = { IHandle 
							- _m2Class = "";
						}
						- m_length = 49;
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 1639cb7b-8b1e-4593-ac99-1b12c91d69cc;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 13469516-2e36-473b-813d-d789cc272db6;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "QR";
							}
							{ IInteractionOperand 
								- _id = GUID eed05f27-c85d-4941-a8c2-8f414a52916b;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _interactionConstraint = "else (ID y Pass)";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 777aa309-0085-4822-9252-ad7925f2b366;
						- _myState = 2048;
						- _name = "interactionOperator_2";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID e53c2307-45e5-47de-b1a7-c499cbb962a5;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- CombinedFragments = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ ICombinedFragment 
										- _id = GUID ba74f05c-11d1-45bd-82c4-ef23e7b8e575;
										- _myState = 2048;
										- _name = "interactionOperator_3";
										- _interactionOperator = "alt";
										- InteractionOperands = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IInteractionOperand 
												- _id = GUID 80a39ab8-0ed7-4b6a-bcc7-d26dcb89866b;
												- _myState = 2048;
												- _name = "interactionOperand_0";
												- _interactionConstraint = "revisar";
											}
											{ IInteractionOperand 
												- _id = GUID 9100f221-8acd-40f1-ab4a-934363fbf981;
												- _myState = 2048;
												- _name = "interactionOperand_1";
												- _interactionConstraint = "cancelar";
											}
										}
									}
								}
								- _interactionConstraint = "primera vez";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 6cc5b213-aca8-4893-bd05-90376b6a352f;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID ffdf39d6-9e9c-4b1d-a3de-69cbd7dfcf9f;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "QR erroneo o Sin alta";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 9594ddac-a270-4e9f-89e7-8dfdaf8c96c1;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "PartitionLine";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,300,0";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "AutoCreateExecutionOccurrence";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Caso de uso 2.1";
			- _lastModifiedTime = "12.5.2013::1:6:0";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 1bd9a37b-1c96-429c-8af3-10939263b0f9;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 9594ddac-a270-4e9f-89e7-8dfdaf8c96c1;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 2;
				{ CGIBox 
					- _id = GUID 9bb5cbd6-afe0-4ee1-b905-2c52e14deb18;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 9ed55bbb-c8dc-44ca-8c56-83cb70a4535e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 81e057fd-eacd-4f40-98d5-6a5511f228ad;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 9bb5cbd6-afe0-4ee1-b905-2c52e14deb18;
					- m_name = { CGIText 
						- m_str = "Navegaci\ón por los contenidos personalizados";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.16667 0 0 1 0 46 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 9bb5cbd6-afe0-4ee1-b905-2c52e14deb18;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 9ed55bbb-c8dc-44ca-8c56-83cb70a4535e;
			}
		}
		{ IMSC 
			- _id = GUID cf2ddd3a-c120-40df-8c62-17e47e2cdec2;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 8;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "EnvironmentLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOccurrence";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,134";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Note";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "250,244,212";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PartitionLine";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,300,0";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "execution_occurrence";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "SequenceDiagram";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "General";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "AutoCreateExecutionOccurrence";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ClassCentricMode";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "CleanupRealized";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "RealizeMessages";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Caso de uso 1.3";
			- _lastModifiedTime = "12.5.2013::12:32:56";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID de4e3a48-58a3-4f03-a3ad-9bdcc53d8a43;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID cf2ddd3a-c120-40df-8c62-17e47e2cdec2;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 23;
				{ CGIBox 
					- _id = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 6f8875e9-2537-4d07-b498-1a75e0d97624;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 096c8169-82cc-40c5-9382-ad4e606f1a39;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 47fba820-31e3-4eed-8201-fa9524b3343c;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.909931 0 0 1 -18.3718 -53 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 118 188  551 188  551 355  118 355  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=72,95>
<frame Id=GUID 5fdae8fb-adb6-4a7e-97e5-4aa4382a0053>
<frame Id=GUID b0416a80-00cd-4a21-9255-ba2e16d58eb2>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 84b67323-253a-41ca-ae70-f258017e42f2;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 108f4272-3d48-4b31-89bf-46bceb9e407f;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.973117 0 0 1 -41.0679 -26 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 147 354  519 354  519 462  147 462  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=108>
<frame Id=GUID 81ad177b-198e-45c6-8a06-a16e0c3d7bb6>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 81ad177b-198e-45c6-8a06-a16e0c3d7bb6;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID abfddba0-55e9-4950-9d59-3eb86ec2193e;
					}
					- m_pParent = GUID 84b67323-253a-41ca-ae70-f258017e42f2;
					- m_name = { CGIText 
						- m_str = "QR erroneo o Sin alta";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 147 354  519 354  519 462  147 462  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 37cf5c91-4080-4a05-aa54-e488c83a28b3;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 3da7b831-f519-44ad-b338-7a3fec9909ee;
					}
					- m_pParent = GUID 5c85c031-39a0-4027-a7f7-911203dd0ddf;
					- m_name = { CGIText 
						- m_str = "desconexi\ón";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 111 735  431 735  431 849  111 849  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "alt";
					- _id = GUID 5c85c031-39a0-4027-a7f7-911203dd0ddf;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID c03d9a53-fe4c-45d5-b616-b1948495f16b;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "interactionOperator_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.06875 0 0 1 -14.6312 -24 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 111 735  431 735  431 849  111 849  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=114>
<frame Id=GUID 37cf5c91-4080-4a05-aa54-e488c83a28b3>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID ef780c70-95d7-44c0-a062-0c2fdba94746;
					- m_type = 97;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 3f0a527f-b20b-4b8c-b290-001b1f52770c;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = ":Usuario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0175 92 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_type = 118;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "ENV";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0175 307 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 50000  96 50000  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscInteractionOccurrence 
					- _id = GUID d41ddf59-e52f-4620-88de-1d0bd2462040;
					- m_type = 172;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOccurrence";
						- _id = GUID edbe6eed-2d53-4986-a676-d27d46400433;
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Caso de uso 2.1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.30556 0 0 0.454545 106 596 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 132  216 132  216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 2db1b852-089b-4f90-8f7f-62bae321a6d0;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 1 alt";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 238 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4c6e4505-0acb-4c03-af12-ba341e977d4d;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 2 alt";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 310 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID a0c2eeea-bcfd-46fa-afd9-2c533b6fe217;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 449 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 925fc656-ffb4-4743-aad4-b80c79a06f2f;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 565 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 12b10ac7-72a7-4125-b230-b7a7e4b56968;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 164 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 04b4c4a3-a654-4591-98c0-18af2f0b03e9;
					- m_type = 120;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
					- m_name = { CGIText 
						- m_str = "Punto 4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_drawBehavior = 0;
					- m_transform = 1.87 0 0 1 0 691 ;
					- m_bIsPreferencesInitialized = 1;
					- m_position = 0 ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 939fa7cc-0440-4bb6-91c4-3d55993e57df;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ace7ee86-0116-4899-ada3-f388bbaffc03;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "registrarCoordenadas()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 386 528  386 547  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 27314 ;
					- m_TargetPort = 48 28400 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f7896d9b-9fdb-413c-8e2e-bc02d3900aab;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3b36ca79-aa43-4c65-85a8-7d0d908d91c3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "capturarQR()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ef780c70-95d7-44c0-a062-0c2fdba94746;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 7657 ;
					- m_TargetPort = 48 7657 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 0228a75f-170f-4976-baf5-314cecbb2761;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 46091292-474a-4ec8-8134-67015bcc2f81;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "comprobarActivacion()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 379 477  379 499  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 24400 ;
					- m_TargetPort = 48 25657 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 795e3c52-f1c3-4237-bb58-9d5781a59acc;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3e82d42a-89d6-4426-868b-6b57017814b5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "indicarIDyPass()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ef780c70-95d7-44c0-a062-0c2fdba94746;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 12286 ;
					- m_TargetPort = 48 12286 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 39752241-c153-47b5-b2d5-a073bc7f00ac;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 58bd2518-0d6e-4ce1-b666-03967f80a3b9;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "desconexion()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3a2b854b-036f-4543-8555-c8561c2f6693;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 385 752  385 789  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 40114 ;
					- m_TargetPort = 48 42229 ;
					- m_bLeft = 0;
				}
				{ CGIMscInteractionOperand 
					- _id = GUID b0416a80-00cd-4a21-9255-ba2e16d58eb2;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 1db4df5f-bad9-4281-bf8e-be0ac575e402;
					}
					- m_pParent = GUID 096c8169-82cc-40c5-9382-ad4e606f1a39;
					- m_name = { CGIText 
						- m_str = "else (ID y Pass)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 118 260  551 260  551 355  118 355  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 5fdae8fb-adb6-4a7e-97e5-4aa4382a0053;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 29c0db87-f4dc-4065-8d2b-96275857bdb0;
					}
					- m_pParent = GUID 096c8169-82cc-40c5-9382-ad4e606f1a39;
					- m_name = { CGIText 
						- m_str = "QR";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 118 188  551 188  551 260  118 260  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 5e0d4323-5a41-4358-b23e-4bd8caaf9618;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 90;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 84b67323-253a-41ca-ae70-f258017e42f2;
					- m_name = { CGIText 
						- m_str = "Finalizar el caso de uso";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.291034 0 0 0.0456204 166.545 401.863 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1099  1084 1099  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 1;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID dc6189cb-6617-4b60-999e-c8f4e5895956;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 6f8875e9-2537-4d07-b498-1a75e0d97624;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IClassifierRole 
						- _id = GUID 3f0a527f-b20b-4b8c-b290-001b1f52770c;
						- _myState = 2048;
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Usuario_actor";
							- _id = GUID c41badc4-79ca-41cb-a7c8-635e31f13532;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						- _name = "ENV";
						- m_eRoleType = SYSTEM_BORDER;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IMessage 
						- _id = GUID 3b36ca79-aa43-4c65-85a8-7d0d908d91c3;
						- _name = "capturarQR";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3f0a527f-b20b-4b8c-b290-001b1f52770c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 46091292-474a-4ec8-8134-67015bcc2f81;
						- _name = "comprobarActivacion";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3e82d42a-89d6-4426-868b-6b57017814b5;
						- _name = "indicarIDyPass";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 3f0a527f-b20b-4b8c-b290-001b1f52770c;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID ace7ee86-0116-4899-ada3-f388bbaffc03;
						- _name = "registrarCoordenadas";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 58bd2518-0d6e-4ce1-b666-03967f80a3b9;
						- _name = "desconexion";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 43965b97-4149-4e4b-a4a6-da01d4f553f2;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- InteractionOccurrences = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IInteractionOccurrence 
						- _id = GUID edbe6eed-2d53-4986-a676-d27d46400433;
						- _name = "Caso de uso 2.1";
						- m_pRefSD = { IHandle 
							- _m2Class = "IMSC";
							- _id = GUID 9594ddac-a270-4e9f-89e7-8dfdaf8c96c1;
						}
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 47fba820-31e3-4eed-8201-fa9524b3343c;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 29c0db87-f4dc-4065-8d2b-96275857bdb0;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "QR";
							}
							{ IInteractionOperand 
								- _id = GUID 1db4df5f-bad9-4281-bf8e-be0ac575e402;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _interactionConstraint = "else (ID y Pass)";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID c03d9a53-fe4c-45d5-b616-b1948495f16b;
						- _myState = 2048;
						- _name = "interactionOperator_2";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID 3da7b831-f519-44ad-b338-7a3fec9909ee;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "desconexi\ón";
							}
						}
					}
					{ ICombinedFragment 
						- _id = GUID 108f4272-3d48-4b31-89bf-46bceb9e407f;
						- _myState = 2048;
						- _name = "interactionOperator_1";
						- _interactionOperator = "alt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID abfddba0-55e9-4950-9d59-3eb86ec2193e;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _interactionConstraint = "QR erroneo o Sin alta";
							}
						}
					}
				}
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 68c07cdf-0a99-4f55-a4f1-a03236f40477;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- _id = GUID 9c2b9ab1-5b6a-4dd8-aed8-d0c659baedc2;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,53,142";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "diagrama auxiliar";
			- _lastModifiedTime = "12.5.2013::12:33:53";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 1002d722-a935-4071-bfe1-63a5c627a7d1;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IUCDiagram";
					- _id = GUID 9c2b9ab1-5b6a-4dd8-aed8-d0c659baedc2;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 3;
				{ CGIClass 
					- _id = GUID 3cefce7c-efa2-4552-8a61-e2d0cbec9993;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 5ff2363b-6502-4cbc-a476-94b3af09fa64;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIBasicClass 
					- _id = GUID d10f1bfd-40eb-4367-b2c5-74f9d244c47e;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Sanitario_actor";
						- _id = GUID 502f7af0-36be-4f67-92ed-c9b218374571;
					}
					- m_pParent = GUID 3cefce7c-efa2-4552-8a61-e2d0cbec9993;
					- m_name = { CGIText 
						- m_str = "Sanitario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 27.3869 50.6655 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIBasicClass 
					- _id = GUID e87ea723-dd5f-4f6b-807b-1bc6a90a500d;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Usuario_actor";
						- _id = GUID c41badc4-79ca-41cb-a7c8-635e31f13532;
					}
					- m_pParent = GUID 3cefce7c-efa2-4552-8a61-e2d0cbec9993;
					- m_name = { CGIText 
						- m_str = "Usuario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 158.387 40.6655 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 3cefce7c-efa2-4552-8a61-e2d0cbec9993;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
		}
	}
	- CollaborationDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ICollaborationDiagram 
			- _id = GUID 0318bfbb-ae33-465a-ac83-942be11b2934;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "AssociationRole";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Classifier_Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,53,142";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Classifier_Role";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,108,72";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Constraint";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "225,217,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Multi_Object";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,168,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Caso de uso 1.3";
			- _lastModifiedTime = "12.7.2013::18:56:51";
			- _graphicChart = { CCollaborationChart 
				- _id = GUID 4ca679a1-e30a-4985-b016-730165108210;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "ICollaboration";
					- _id = GUID d2866c69-1941-4a6f-83c6-29300dc01519;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 4096;
				- m_bIsPreferencesInitialized = 1;
				- elementList = 15;
				{ CGIBox 
					- _id = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
					- m_type = 154;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID d2866c69-1941-4a6f-83c6-29300dc01519;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClassifierRole 
					- _id = GUID a7f46186-653a-479f-99cc-5eb00949799e;
					- m_type = 158;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
					}
					- m_pParent = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
					- m_name = { CGIText 
						- m_str = ":Usuario_actor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0489381 0 0 0.124343 103.387 23.665 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClassifierRole 
					- _id = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_type = 156;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
					}
					- m_pParent = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
					- m_name = { CGIText 
						- m_str = "Base Datos:BDU";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0974729 0 0 0.0671642 308 119 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 1072  1108 1072  1108 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationRole 
					- _id = GUID e80e796c-5d89-422b-a261-2f0b99057429;
					- m_type = 159;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationRole";
						- _id = GUID c7362e1c-6bda-48c7-bb5c-97e25872b51b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a7f46186-653a-479f-99cc-5eb00949799e;
					- m_sourceType = 'F';
					- m_pTarget = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "associationrole_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 952 847 ;
					- m_TargetPort = 739 149 ;
				}
				{ CGIMessageLabel 
					- _id = GUID fa7312f7-af8a-402c-8c2c-7643fd67dce4;
					- m_type = 160;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 56901734-2741-4463-9760-523056fd80f6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "1. CapturaQR()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -44 -7  45 -7  45 8  -44 8  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pCommunicationConnection = GUID e80e796c-5d89-422b-a261-2f0b99057429;
					- _percent = 52;
				}
				{ CGIAssociationRole 
					- _id = GUID efd6f751-d782-4c8f-b17d-d9bb5900b23b;
					- m_type = 159;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationRole";
						- _id = GUID e2675c47-9404-4c5d-8af1-8bbe108199c3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a7f46186-653a-479f-99cc-5eb00949799e;
					- m_sourceType = 'F';
					- m_pTarget = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "associationrole_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 748 1209 ;
					- m_TargetPort = 492 819 ;
				}
				{ CGIMessageLabel 
					- _id = GUID b140655a-6196-428b-8f59-2af7fdf5b8ce;
					- m_type = 160;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c39f95fe-5b29-4916-8130-efa3f682438d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "2. LoginDesdeWeb()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -5 -8  106 -8  106 6  -5 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 184 168 ;
						- m_nHorizontalSpacing = -32;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pCommunicationConnection = GUID efd6f751-d782-4c8f-b17d-d9bb5900b23b;
					- _percent = 73;
				}
				{ CGIClassifierRole 
					- _id = GUID 483b90ac-e000-452c-b567-29982894c70b;
					- m_type = 156;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 7bb26383-6319-46bd-b82c-1db90e89d8ff;
					}
					- m_pParent = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
					- m_name = { CGIText 
						- m_str = "RegistraCoordenadas:Evento";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0974729 0 0 0.0671642 562 127 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 1072  1108 1072  1108 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClassifierRole 
					- _id = GUID 1d849417-f92d-4daf-bfa7-a120b9345d11;
					- m_type = 156;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 6c108318-883b-4342-98ef-1b1cf799fff6;
					}
					- m_pParent = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
					- m_name = { CGIText 
						- m_str = "InformarUsuario:Evento";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0974729 0 0 0.0671642 318 296 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 1072  1108 1072  1108 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationRole 
					- _id = GUID a5253288-1c40-49dc-a7bf-9c1fe78b8688;
					- m_type = 159;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationRole";
						- _id = GUID d0f0ed33-fb1e-4524-8ad7-d8dcd486d8b5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1d849417-f92d-4daf-bfa7-a120b9345d11;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "associationrole_3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 308 730 ;
					- m_TargetPort = 205 283 ;
				}
				{ CGIAssociationRole 
					- _id = GUID c010d3c8-2c82-4fb0-bfc7-b2bcf8474386;
					- m_type = 159;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationRole";
						- _id = GUID 61f10d91-275c-467f-9fa7-ce3f13a80c1c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_sourceType = 'F';
					- m_pTarget = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "associationrole_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 328 69  392 69  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 205 119 ;
					- m_TargetPort = 862 134 ;
				}
				{ CGIMessageLabel 
					- _id = GUID d74814e6-bbb4-4c78-8228-2ff8fcd0d1f5;
					- m_type = 160;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 862135b3-708f-4e89-967a-db2012ba1ae5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "3. compruebaUsuario()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -44 -7  45 -7  45 8  -44 8  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pCommunicationConnection = GUID c010d3c8-2c82-4fb0-bfc7-b2bcf8474386;
					- _percent = 54;
				}
				{ CGIAssociationRole 
					- _id = GUID e084bae0-03cc-4e8d-b6e8-a02e49c05cd7;
					- m_type = 159;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationRole";
						- _id = GUID 86f1c182-e2d2-488c-b998-a8060f0066a3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8192;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b754a9ef-f181-425d-b417-f0dc96c7ee42;
					- m_sourceType = 'F';
					- m_pTarget = GUID 483b90ac-e000-452c-b567-29982894c70b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "associationrole_4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 964 447 ;
					- m_TargetPort = 472 328 ;
				}
				{ CGIMessageLabel 
					- _id = GUID 26cf4ff5-a602-4631-86d6-f98ac73068ff;
					- m_type = 160;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d81144ba-4b70-4b83-8a38-771aa09b1b15;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "4. UsuarioActivado()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -8  109 -8  109 6  -6 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 438 144 ;
						- m_nHorizontalSpacing = -28;
						- m_nVerticalSpacing = 1;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pCommunicationConnection = GUID e084bae0-03cc-4e8d-b6e8-a02e49c05cd7;
					- _percent = 69;
				}
				{ CGIMessageLabel 
					- _id = GUID 1ef10d9e-30c5-4a1d-9c1f-ffed9fb50e15;
					- m_type = 160;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 80ab2297-f586-4162-bd3a-941cf87a972c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "5. UsuarioNoActivado()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -44 -7  45 -7  45 8  -44 8  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pCommunicationConnection = GUID a5253288-1c40-49dc-a7bf-9c1fe78b8688;
					- _percent = 49;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 81e6d58c-aec3-430f-8cd8-6aa1d2b3f024;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID f37567ff-e040-4aae-bbd0-9a63eca54fee;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID d2866c69-1941-4a6f-83c6-29300dc01519;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 4;
					- value = 
					{ IClassifierRole 
						- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
						- _myState = 2048;
						- m_eRoleType = ACTOR;
						- m_pBase = { IHandle 
							- _m2Class = "IActor";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Usuario_actor";
							- _id = GUID c41badc4-79ca-41cb-a7c8-635e31f13532;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						- _name = "Base Datos";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "BDU";
							- _id = GUID 6332044c-8c36-47fc-a67b-5d9d56d09b8b;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 7bb26383-6319-46bd-b82c-1db90e89d8ff;
						- _name = "RegistraCoordenadas";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Evento";
							- _id = GUID c8021acb-09e9-4a92-9c6c-c21cd9a7e909;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 6c108318-883b-4342-98ef-1b1cf799fff6;
						- _name = "InformarUsuario";
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Evento";
							- _id = GUID c8021acb-09e9-4a92-9c6c-c21cd9a7e909;
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- AssociationRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IAssociationRole 
						- _id = GUID c7362e1c-6bda-48c7-bb5c-97e25872b51b;
						- _myState = 2048;
						- _name = "associationrole_0";
						- m_fAssocType1 = UNSPECIFIED;
						- m_fAssocType2 = UNSPECIFIED;
						- m_pFormalAssoc1 = { IHandle 
							- _m2Class = "";
						}
						- m_pFormalAssoc2 = { IHandle 
							- _m2Class = "";
						}
						- m_pSource = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
						}
						- m_pTarget = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
					}
					{ IAssociationRole 
						- _id = GUID e2675c47-9404-4c5d-8af1-8bbe108199c3;
						- _myState = 2048;
						- _name = "associationrole_1";
						- m_fAssocType1 = UNSPECIFIED;
						- m_fAssocType2 = UNSPECIFIED;
						- m_pFormalAssoc1 = { IHandle 
							- _m2Class = "";
						}
						- m_pFormalAssoc2 = { IHandle 
							- _m2Class = "";
						}
						- m_pSource = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
						}
						- m_pTarget = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
					}
					{ IAssociationRole 
						- _id = GUID d0f0ed33-fb1e-4524-8ad7-d8dcd486d8b5;
						- _myState = 2048;
						- _name = "associationrole_3";
						- m_fAssocType1 = UNSPECIFIED;
						- m_fAssocType2 = UNSPECIFIED;
						- m_pFormalAssoc1 = { IHandle 
							- _m2Class = "";
						}
						- m_pFormalAssoc2 = { IHandle 
							- _m2Class = "";
						}
						- m_pSource = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pTarget = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6c108318-883b-4342-98ef-1b1cf799fff6;
						}
					}
					{ IAssociationRole 
						- _id = GUID 61f10d91-275c-467f-9fa7-ce3f13a80c1c;
						- _myState = 2048;
						- _name = "associationrole_2";
						- m_fAssocType1 = UNSPECIFIED;
						- m_fAssocType2 = UNSPECIFIED;
						- m_pFormalAssoc1 = { IHandle 
							- _m2Class = "";
						}
						- m_pFormalAssoc2 = { IHandle 
							- _m2Class = "";
						}
						- m_pSource = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pTarget = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
					}
					{ IAssociationRole 
						- _id = GUID 86f1c182-e2d2-488c-b998-a8060f0066a3;
						- _myState = 2048;
						- _name = "associationrole_4";
						- m_fAssocType1 = UNSPECIFIED;
						- m_fAssocType2 = UNSPECIFIED;
						- m_pFormalAssoc1 = { IHandle 
							- _m2Class = "";
						}
						- m_pFormalAssoc2 = { IHandle 
							- _m2Class = "";
						}
						- m_pSource = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pTarget = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7bb26383-6319-46bd-b82c-1db90e89d8ff;
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IMessage 
						- _id = GUID 56901734-2741-4463-9760-523056fd80f6;
						- _name = "CapturaQR";
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "IAssociationRole";
							- _id = GUID c7362e1c-6bda-48c7-bb5c-97e25872b51b;
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c39f95fe-5b29-4916-8130-efa3f682438d;
						- _name = "LoginDesdeWeb";
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "IAssociationRole";
							- _id = GUID e2675c47-9404-4c5d-8af1-8bbe108199c3;
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 5dfa670e-835a-4998-99e4-6b2855de53c2;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 862135b3-708f-4e89-967a-db2012ba1ae5;
						- _name = "compruebaUsuario";
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "IAssociationRole";
							- _id = GUID 61f10d91-275c-467f-9fa7-ce3f13a80c1c;
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d81144ba-4b70-4b83-8a38-771aa09b1b15;
						- _name = "UsuarioActivado";
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "IAssociationRole";
							- _id = GUID 86f1c182-e2d2-488c-b998-a8060f0066a3;
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 7bb26383-6319-46bd-b82c-1db90e89d8ff;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 80ab2297-f586-4162-bd3a-941cf87a972c;
						- _name = "UsuarioNoActivado";
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "IAssociationRole";
							- _id = GUID d0f0ed33-fb1e-4524-8ad7-d8dcd486d8b5;
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 6c108318-883b-4342-98ef-1b1cf799fff6;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID eaecd34a-632d-467a-b4b5-3d1062a7a29f;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- p_MessageHandler = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ CollEvent 
						- _id = GUID 488fdb81-7e69-4d8a-8eed-f120cba40701;
						- first = UNSPECIFIED;
						- second = GUID 56901734-2741-4463-9760-523056fd80f6;
					}
					{ CollEvent 
						- _id = GUID 81371a04-9390-4a2b-96b2-10f3f8b59f27;
						- first = UNSPECIFIED;
						- second = GUID c39f95fe-5b29-4916-8130-efa3f682438d;
					}
					{ CollEvent 
						- _id = GUID d960f51f-83ea-49d8-bbb8-d96ebd42c816;
						- first = UNSPECIFIED;
						- second = GUID 862135b3-708f-4e89-967a-db2012ba1ae5;
					}
					{ CollEvent 
						- _id = GUID 98fdf28c-ded6-40c1-b6e8-16923db8f1e7;
						- first = UNSPECIFIED;
						- second = GUID d81144ba-4b70-4b83-8a38-771aa09b1b15;
					}
					{ CollEvent 
						- _id = GUID cdb667f0-5c26-4d50-a3c8-cfecaaf84587;
						- first = UNSPECIFIED;
						- second = GUID 80ab2297-f586-4162-bd3a-941cf87a972c;
					}
				}
			}
		}
	}
	- PanelDiagrams = { IRPYRawContainer 
		- size = 0;
	}
}

