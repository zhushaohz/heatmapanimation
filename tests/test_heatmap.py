import heatmapanimation as hma
import pytest

def test_run_x():
    heatmap = hma.Heatmap()
    heatmap.region = '北京'
    result = heatmap.run_x()
    assert result == 'success'

def test_run():
    heatmap = hma.Heatmap()
    heatmap.region = '北京'
    result = heatmap.run_x()
    assert result == 'success'

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test.py'])