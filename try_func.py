
str_file_input = r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\WatershedMap_kmb.txt"


def WatershedMap_func(str_file_input):
    import arcpy
    import os

    with open(str_file_input, "r") as txtfile:
        contents = txtfile.readlines()
        txtfile.close()

    for lyrName in lyrList:
        mxd = arcpy.mapping.MapDocument(str_dir_main + "\\" + str_mxd_blank)
        df = arcpy.mapping.ListDataFrames(mxd, str_df_cur)[0]
        str_layerfile = os.path.join(str_dir_main, lyr_save_pre + lyrName + lyr_save_post)
        addlayer = arcpy.mapping.Layer(str_layerfile)
        arcpy.mapping.AddLayer(df, addlayer, "BOTTOM")
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()
        mxd.saveACopy(str_dir_main + "\\" + str_mxd_save_pre + lyrName + str_mxd_save_post)

        del addlayer, df, mxd


WatershedMap_func(str_file_input)

