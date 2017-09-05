#coding: utf-8
import pandas
import math
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

dataframe = None
file_name = None


def list_of_data(val):
    try:
        data = []
        for row in dataframe.index.values:
            for column in dataframe.columns:
                if column == val:

                    if dataframe.get_value(row, column) != val and dataframe.get_value(row, column) != None:
                        num = float(dataframe.get_value(row, column))
                        if math.isnan(num) == False:
                            data.append(num)
                        else:
                            data.append(0)
        return data
    except Exception as e:
        print e

def __avg__(lst):
    return sum(lst)/len(lst)

def truncate(lst):
    return stats.trim_mean(lst, 0.2)

def variance(lst):
    variance_sum = []
    avg =  __avg__(lst)
    total = len(lst)-1
    for value in lst:
        variance_sum.append((value - avg)**2)
    return sum(variance_sum)/total

def standard_deviation(lst):
    return math.sqrt(variance(lst))

def mean_absolute_deviation(lst):
    deviation_sum = []
    avg =  __avg__(lst)
    total = len(lst)
    for value in lst:
        deviation_sum.append(math.fabs(value - avg))
    return sum(deviation_sum)/total

def upper_lower_quartile(lst):
    upper_quartile = np.percentile(lst, 75)
    lower_quartile = np.percentile(lst, 25)
    return upper_quartile, lower_quartile

def mean(lst):
    return np.mean(lst)

def median(lst):
    return np.median(lst)

def pearson_correlation(lst1,lst2):
    result = []
    divide_by_lst1 = []
    divide_by_lst2 = []
    lst1_avg = __avg__(lst1)

    lst2_avg = __avg__(lst2)

    for val1, val2 in zip(lst1, lst2):
        result.append((val1 - lst1_avg)*(val2 - lst2_avg))

    for val1, val2 in zip(lst1, lst2):
        divide_by_lst1.append((val1 - lst1_avg)**2)
        divide_by_lst2.append((val2 - lst2_avg)**2)

    divide_by = sum(divide_by_lst1)*sum(divide_by_lst2)
    divide_by = math.sqrt(divide_by)

    return sum(result)/divide_by

def spearman_correlation(lst1,lst2):
    result = []
    for val1, val2 in zip(lst1, lst2):
        result.append((val1 - val2)**2)
    divide_by = (len(lst1)**3) - len(lst1)

    return 1-(6*sum(result)/divide_by)

def min_max(lst):
    return min(lst), max(lst)


def define_dataframe(csv_file):
    try:
        col_name = ['nu_ano','co_grupo','co_ies','co_catad','co_orgac','co_munic_curso','co_uf_curso','co_regiao_curso',
                    'co_curso','nu_idade','tp_sexo','ano_fim_2g','ano_in_grad','tp_semestre','in_matutino','in_vespertino',
                    'in_noturno','id_status','amostra','tp_inscricao','tp_def_fis','tp_def_vis','tp_def_aud','nu_item_ofg',
                    'nu_item_ofg_z','nu_item_ofg_x','nu_item_ofg_n','vt_gab_ofg_orig','vt_gab_ofg_fin','nu_item_oce',
                    'nu_item_oce_z','nu_item_oce_x','nu_item_oce_n','vt_gab_oce_orig','vt_gab_oce_fin','tp_pres',
                    'tp_pr_ger','tp_pr_ob_fg','tp_pr_di_fg','tp_pr_ob_ce','tp_pr_di_ce','tp_sfg_d1','tp_sfg_d2',
                    'tp_sce_d1','tp_sce_d2','tp_sce_d3','vt_esc_ofg','vt_ace_ofg','vt_esc_oce','vt_ace_oce',
                    'nt_obj_fg','nt_fg_d1_pt','nt_fg_d1_ct','nt_fg_d1','nt_fg_d2_pt','nt_fg_d2_ct','nt_fg_d2',
                    'nt_dis_fg','nt_fg','nt_obj_ce','nt_ce_d1','nt_ce_d2','nt_ce_d3','nt_dis_ce','nt_ce','nt_ger',
                    'qp_i1','qp_i2','qp_i3','qp_i4','qp_i5','qp_i6','qp_i7','qp_i8','qp_i9','qe_i1','qe_i2','qe_i3',
                    'qe_i4','qe_i5','qe_i6','qe_i7','qe_i8','qe_i9','qe_i10','qe_i11','qe_i12','qe_i13','qe_i14','qe_i15',
                    'qe_i16','qe_i17','qe_i18','qe_i19','qe_i20','qe_i21','qe_i22','qe_i23','qe_i24','qe_i25','qe_i26','qe_i27',
                    'qe_i28','qe_i29','qe_i30','qe_i31','qe_i32','qe_i33','qe_i34','qe_i35','qe_i36','qe_i37','qe_i38',
                    'qe_i39','qe_i40','qe_i41','qe_i42','qe_i43','qe_i44','qe_i45','qe_i46','qe_i47','qe_i48','qe_i49',
                    'qe_i50','qe_i51','qe_i52','qe_i53','qe_i54','qe_i55','qe_i56','qe_i57','qe_i58','qe_i59','qe_i60',
                    'qe_i61','qe_i62','qe_i63','qe_i64','qe_i65','qe_i66','qe_i67','qe_i68','qe_i69','qe_i70','qe_i71',
                    'qe_i72','qe_i73','qe_i74','qe_i75','qe_i76','qe_i77','qe_i78','qe_i79','qe_i80','qe_i81']
        global dataframe
        dataframe = pandas.read_csv(csv_file, sep=';', names=col_name)
        global file_name
        file_name = csv_file
    except pandas.io.common.EmptyDataError:
        raise Exception('Not a valid file.')


def print_dataframe():
    try:
        assert dataframe is not None, 'Dataframe was not created.'
        print('\n')
        print(dataframe)
        print('\n')
    except AssertionError, e:
        print(e.args[0])

def age_avg():
    age = list_of_data('nu_idade')

    print '\n'*4
    print "IDADE"
    print "Total de dados analisados: " +  str(len(age))
    print "Media: " + str(__avg__(age))
    print "Mean: " + str(mean(age))
    print "Mediana: " + str(median(age))
    print "Media truncada: " + str(truncate(age))
    print "Variança: " + str(variance(age))
    print "Standard Deviation: "+ str(standard_deviation(age))
    upper, lower =upper_lower_quartile(age)
    print "Upper Quartile: " + str(upper)
    print "Lower Quartile: " + str(lower)
    min_age, max_age =min_max(age)
    print "Menor idade: " + str(min_age)
    print "Maior idade: " + str(max_age)


    plt.figure("Histogram People age")
    plt.hist(age)
    plt.title('Age distribution')
    plt.xlabel("Age")
    plt.ylabel("Quantity")
    plt.show()


    plt.figure("BoxPlot People age")
    plt.boxplot(age)
    plt.ylabel("Age")
    plt.show()

def grad_school():
    anoGrad = list_of_data('ano_fim_2g')
    print '\n'*4
    print "ANO DE GRADUACAO NO COLEGIO"
    print "Total de dados analisados: " + str(len(anoGrad))
    print "Media: " + str(__avg__(anoGrad))
    print "Mean: " + str(mean(anoGrad))
    print "Median: " + str(median(anoGrad))
    print "Media truncada: " + str(truncate(anoGrad))
    upper, lower =upper_lower_quartile(anoGrad)
    print "Upper Quartile: " + str(upper)
    print "Lower Quartile: " + str(lower)

    min_year_grad, max_year_grad =min_max(anoGrad)
    print "Ano minimo de graduação no Colégio: " + str(min_year_grad)
    print "Ano máximo de graduação no Colégio: " + str(max_year_grad)

    plt.figure("Histogram Year of High School Graduation")
    plt.hist(anoGrad)
    plt.title('Year of High School Graduation distribution')
    plt.xlabel("Year")
    plt.ylabel("Quantity")

    plt.figure("BoxPlot Year of High School Graduation")
    plt.ylabel("Year")
    plt.boxplot(anoGrad)

    plt.show()


def grad_school_ini_college():
    ano2Grad = list_of_data('ano_fim_2g')
    anoFIni = list_of_data('ano_in_grad')
    print '\n'*4
    print "ANO DE GRADUACAO NO COLEGIO VS ANO DE INICIO DA FACULDADE"
    print "Total de dados analisados: " + str(len(ano2Grad))
    print "Correlação de Pearson: " + str(pearson_correlation(ano2Grad,anoFIni))
    print "Correlação de Spearman: " + str(spearman_correlation(ano2Grad,anoFIni))

    plt.figure("ScatterPlot Year of High School Graduation - Start College")
    plt.xlabel("School Grad Year")
    plt.ylabel("College Start Year")
    plt.scatter(ano2Grad,anoFIni)


    # #############
    # upperE, lowerE =upper_lower_quartile(ano2Grad)
    # print "Ano de Graduacao no Ensino Medio "
    # print "Upper Quartile: " + str(upperE)
    # print "Lower Quartile: " + str(lowerE)
    #
    # upperF, lowerF =upper_lower_quartile(anoFIni)
    # print "Ano de inicio na faculdade"
    # print "Upper Quartile: " + str(upperF)
    # print "Lower Quartile: " + str(lowerF)
    #
    # plt.figure("BoxPlot Year of High School Graduation - start College")
    # plt.ylabel("Year")
    # plt.boxplot([ano2Grad,anoFIni])
    #
    # plt.ylabel("Year")
    # ##################

    plt.show()


def age_grade_correlation():
    age = list_of_data('nu_idade')
    grade = list_of_data('nt_ger')


    print '\n'*4
    print "IDADE VS NOTA"
    print "Total de dados analisados: " + str(len(age))
    print "Correlação de Pearson: " + str(pearson_correlation(age,grade))
    print "Correlação de Spearman: " + str(spearman_correlation(age,grade))


    plt.figure("ScatterPlot Age - Grade")
    plt.xlabel("Age")
    plt.ylabel("grade")
    plt.scatter(age,grade)
    plt.show()




define_dataframe("teste_enade_2014.csv")

age_avg()
grad_school()
grad_school_ini_college()
age_grade_correlation()