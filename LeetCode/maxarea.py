���� n ���Ǹ����� a1��a2��...��an��ÿ�������������е�һ���� (i, ai) ���������ڻ� n ����ֱ�ߣ���ֱ�� i �������˵�ֱ�Ϊ (i, ai) �� (i, 0)���ҳ����е������ߣ�ʹ�������� x �Ṳͬ���ɵ�����������������ˮ��

˵�����㲻����б�������� n ��ֵ����Ϊ 2��


ͼ�д�ֱ�ߴ����������� [1,8,6,2,5,4,8,3,7]���ڴ�����£������ܹ�����ˮ����ʾΪ��ɫ���֣������ֵΪ 49��

 class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxarea = 0
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if maxarea < area:
                maxarea = area
        return maxarea