import arcpy
import os

# base folder
str_dir_main = r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps"
str_mxd_blank = r"Upper_Yaquina_TMDL_Blank_ME.mxd"
str_df_cur = r"Layers"
str_lyr_cur = r"UY_*.lyr"
str_mxd_save_pre = r"Upper_Yaquina_TMDL_UY_"
str_mxd_save_post = r".mxd"

mxd = arcpy.mapping.MapDocument(str_dir_main + "\\" + str_mxd_blank)
df = arcpy.mapping.ListDataFrames(mxd, str_df_cur)[0]
lyrList =
walk = arcpy.da.Walk(str_dir_main, datatype="Layer")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        layerfile = os.path.join(dirpath, filename)
        addlayer = arcpy.mapping.Layer(layerfile)
        arcpy.mapping.AddLayer(df, addlayer, "BOTTOM")
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()
        mxd.saveACopy(str_dir_main + "\\" + str_mxd_save_pre + str_mxd_save_post)



del addlayer, mxd, df




addLayer = arcpy.mapping.Layer(str_dir_main + "\\" + str_lyr_cur)

arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
arcpy.RefreshTOC()
arcpy.RefreshActiveView()

mxd.saveACopy(str_dir_main + "\\" + str_mxd_save)

del mxd, df, addLayer
