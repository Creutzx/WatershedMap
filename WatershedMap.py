import arcpy
import os


str_dir_main = r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps"
str_mxd_blank = r"Upper_Yaquina_TMDL_Blank_ME.mxd"
str_df_cur = r"Layers"
str_lyr_cur = r"UY_*.lyr"
str_mxd_save_pre = r"Upper_Yaquina_TMDL_UY_"
str_mxd_save_post = r".mxd"
lyr_mxd_save_post = r".lyr"

mxd = arcpy.mapping.MapDocument(str_dir_main + "\\" + str_mxd_blank)
df = arcpy.mapping.ListDataFrames(mxd, str_df_cur)[0]
lyrList = ["Elev", "Precip", "Geo"]

for lyrName in lyrList:
    layerfile = (str_dir_main + "\\" + lyrName + lyr_mxd_save_post)
    addlayer = arcpy.mapping.Layer(layerfile)
    arcpy.mapping.AddLayer(df, addlayer, "BOTTOM")
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
    mxd.saveACopy(str_dir_main + "\\" + str_mxd_save_pre + LyrName + str_mxd_save_post)


del addlayer, mxd, df

