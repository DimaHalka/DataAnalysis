**Иерархический кластерный анализ (hierarchical clustering)** — это метод кластеризации в машинном обучении, который строит иерархию кластеров. Он используется для объединения похожих объектов в группы (кластеры) без заранее заданного числа кластеров. Относится к методам неконтролируемого обучения (unsupervised learning). Не требует заранее заданного количества кластеров (в отличие от, например, K-средних). Представляет результат в виде дендрограммы — дерева, отражающего порядок объединения (или разбиения) объектов. Кластеризация может быть двух видов.

**Агломеративная** (снизу вверх, наиболее популярна)
- Каждый объект — отдельный кластер.
- Постепенно кластеры объединяются, пока не останется один.
- Объединение основано на мере схожести (например, евклидово расстояние).

**Дивизивная** (сверху вниз)
- Начинаем с одного большого кластера.
- Постепенно разделяем на более мелкие кластеры.

Метрики похожести/непохожести кластеров:
- Single linkage (ближайший сосед)
- Complete linkage (дальний сосед)
- Average linkage (среднее расстояние)
- Ward’s method (минимизация внутрикластерной дисперсии)

Иерархическая кластеризация может использоваться как предобработка (feature engineering) или для анализа структуры данных.

При агломеративной кластеризации (снизу вверх) **критерий останова** определяет, на каком этапе нужно прекратить объединение кластеров. В базовом виде алгоритм продолжается до тех пор, пока не останется один кластер, включающий все объекты. Но в реальных задачах останавливаются раньше — по одному из следующих критериев останова:

- Заданное число кластеров (n_clusters). Самый распространённый способ.
Например sklearn.cluster.AgglomerativeClustering(n_clusters=k).

- Порог расстояния (distance_threshold)
Объединение прекращается, когда расстояние между ближайшими кластерами превышает заданный порог.

- Минимальный прирост расстояния (или максимальный разрыв)
Анализ дендрограммы: ищется самый большой скачок расстояния между двумя последовательными объединениями.

- Визуальный анализ дендрограммы
Часто используется как эвристика: обрезается дерево на определённой "высоте", где визуально различимы отдельные кластеры.
