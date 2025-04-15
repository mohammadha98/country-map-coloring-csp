import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch

mpl.rcParams['font.family'] = 'Arial'
try:
    mpl.font_manager.fontManager.addfont('Vazir.ttf')
    mpl.rcParams['font.family'] = 'Vazir'
except:
    pass

mpl.rcParams['axes.unicode_minus'] = False


class MapVisualizer:
    def __init__(self, provinces, neighbors):
        self.provinces = provinces
        self.neighbors = neighbors
        self.graph = self._create_graph()
        self.color_map = {
            'قرمز': 'red',
            'آبی': 'blue',
            'سبز': 'green',
            'زرد': 'yellow'
        }
        
    def _create_graph(self):
        G = nx.Graph()
        
        for province in self.provinces:
            G.add_node(province)
        
        for province, neighbors_list in self.neighbors.items():
            for neighbor in neighbors_list:
                G.add_edge(province, neighbor)
        
        return G
    
    def visualize(self, coloring=None, save_path=None):
        plt.figure(figsize=(12, 10))
        
        pos = nx.spring_layout(self.graph, seed=42, k=0.3)
        
        if coloring:
            node_colors = [self.color_map[coloring[node]] for node in self.graph.nodes()]
        else:
            node_colors = ['lightgray' for _ in self.graph.nodes()]
        
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1500,
            font_size=10,
            font_weight='bold',
            edge_color='gray',
            width=1.5,
            alpha=0.8
        )
        
        if coloring:
            legend_elements = [Patch(facecolor=color, label=name) 
                              for name, color in self.color_map.items() 
                              if name in coloring.values()]
            plt.legend(handles=legend_elements, loc='upper right')
        
        plt.title('نقشه رنگ‌آمیزی شده استان‌های ایران', fontsize=16)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"تصویر در مسیر {save_path} ذخیره شد.")
        
        plt.show()
    
    def visualize_step_by_step(self, steps, delay=1.0, save_path=None):
        for i, coloring in enumerate(steps):
            plt.figure(figsize=(12, 10))
            
            pos = nx.spring_layout(self.graph, seed=42, k=0.3)
            
            node_colors = []
            for node in self.graph.nodes():
                if node in coloring:
                    node_colors.append(self.color_map[coloring[node]])
                else:
                    node_colors.append('lightgray')
            
            nx.draw(
                self.graph,
                pos,
                with_labels=True,
                node_color=node_colors,
                node_size=1500,
                font_size=10,
                font_weight='bold',
                edge_color='gray',
                width=1.5,
                alpha=0.8
            )
            
            legend_elements = [Patch(facecolor=color, label=name) 
                              for name, color in self.color_map.items() 
                              if name in coloring.values()]
            plt.legend(handles=legend_elements, loc='upper right')
            
            plt.title(f'گام {i+1}: نقشه رنگ‌آمیزی شده استان‌های ایران', fontsize=16)
            
            if save_path:
                step_save_path = save_path.format(i+1)
                plt.savefig(step_save_path, dpi=300, bbox_inches='tight')
                print(f"تصویر گام {i+1} در مسیر {step_save_path} ذخیره شد.")
            
            plt.pause(delay)
            
            if i < len(steps) - 1:
                plt.close()
        
        plt.show()